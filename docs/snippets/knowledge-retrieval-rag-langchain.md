---
name: "Knowledge Retrieval (RAG) with LangChain and LangGraph"
objective: "Demonstrates a full RAG pipeline using LangChain for data processing and LangGraph for building the retrieval and generation graph."
how_to_run: "Requires LangChain, LangGraph, Weaviate, and an OpenAI API key. Run with `python your_script_name.py`."
from_note: "../patterns/knowledge-retrieval-rag.md"
---

# RAG with LangChain and LangGraph

This snippet showcases a complete Retrieval-Augmented Generation (RAG) application. It uses LangChain for loading and processing documents, and LangGraph to define a stateful graph that orchestrates the retrieval and generation steps.

## Code Example

```python
import os
import requests
from typing import List, Dict, Any, TypedDict
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import StateGraph, END
import weaviate
from weaviate.embedded import EmbeddedOptions
import dotenv

# Load environment variables (e.g., OPENAI_API_KEY)
dotenv.load_dotenv()

# --- 1. Data Preparation (Preprocessing) ---
# Load data
url = "https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)
loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

# Chunk documents
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Embed and store chunks in Weaviate
client = weaviate.Client(
    embedded_options = EmbeddedOptions()
)
vectorstore = Weaviate.from_documents(
    client = client,
    documents = chunks,
    embedding = OpenAIEmbeddings(),
    by_text = False
)

# Define the retriever
retriever = vectorstore.as_retriever()

# Initialize LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# --- 2. Define the State for LangGraph ---
class RAGGraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str

# --- 3. Define the Nodes (Functions) ---
def retrieve_documents_node(state: RAGGraphState) -> RAGGraphState:
    """Retrieves documents based on the user's question."""
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question, "generation": ""}

def generate_response_node(state: RAGGraphState) -> RAGGraphState:
    """Generates a response using the LLM based on retrieved documents."""
    question = state["question"]
    documents = state["documents"]

    # Prompt template
    template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
    Question: {question}
    Context: {context}
    Answer: """
    prompt = ChatPromptTemplate.from_template(template)

    # Format the context from the documents
    context = "\n\n".join([doc.page_content for doc in documents])

    # Create the RAG chain
    rag_chain = prompt | llm | StrOutputParser()

    # Invoke the chain
    generation = rag_chain.invoke({"context": context, "question": question})
    return {"question": question, "documents": documents, "generation": generation}

# --- 4. Build the LangGraph Graph ---
workflow = StateGraph(RAGGraphState)

# Add nodes
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("generate", generate_response_node)

# Set the entry point
workflow.set_entry_point("retrieve")

# Add edges (transitions)
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the graph
app = workflow.compile()

# --- 5. Run the RAG Application ---
if __name__ == "__main__":
    print("\n--- Running RAG Query ---")
    query = "What did the president say about Justice Breyer"
    inputs = {"question": query}
    for s in app.stream(inputs):
        print(s)

    print("\n--- Running another RAG Query ---")
    query_2 = "What did the president say about the economy?"
    inputs_2 = {"question": query_2}
    for s in app.stream(inputs_2):
        print(s)
```

## How It Works

1.  **Data Preparation**: The script fetches text data, splits it into chunks, and embeds and stores these chunks in a Weaviate vector store.
2.  **State Definition**: A `RAGGraphState` class is defined to manage the state of the graph, holding the question, retrieved documents, and the generated response.
3.  **Graph Nodes**:
    *   `retrieve_documents_node`: This node takes a question from the state and uses the Weaviate retriever to find relevant documents.
    *   `generate_response_node`: This node takes the retrieved documents and the original question, formats them into a prompt, and uses an LLM to generate an answer.
4.  **Graph Construction**: A `StateGraph` is created. The `retrieve` and `generate` nodes are added, and edges are defined to create a flow from retrieval to generation.
5.  **Execution**: The compiled graph is run with a sample question, streaming the output as the state transitions through the graph.