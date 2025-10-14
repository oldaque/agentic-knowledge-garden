import asyncio
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough

# --- Configuration ---
try:
    llm: Optional[ChatOpenAI] = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
except Exception as e:
    llm = None

# --- Define Independent Chains ---
summarize_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Summarize the following topic concisely:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

questions_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Generate three interesting questions about the following topic:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

# --- Build the Parallel + Synthesis Chain ---
map_chain = RunnableParallel(
    {
        "summary": summarize_chain,
        "questions": questions_chain,
        "topic": RunnablePassthrough(),
    }
)

synthesis_prompt = ChatPromptTemplate.from_messages([
    ("system", """Based on the following information:
    Summary: {summary}
    Related Questions: {questions}
    Synthesize a comprehensive answer."""),
    ("user", "Original topic: {topic}")
])

full_parallel_chain = map_chain | synthesis_prompt | llm | StrOutputParser()

# --- Run the Chain ---
async def run_parallel_example(topic: str) -> None:
    if not llm:
        return
    response = await full_parallel_chain.ainvoke(topic)
    print(response)

if __name__ == "__main__":
    test_topic = "The history of space exploration"
    asyncio.run(run_parallel_example(test_topic))
