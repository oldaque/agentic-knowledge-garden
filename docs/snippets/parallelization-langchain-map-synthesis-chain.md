---
name: "Parallelization with LangChain: Map and Synthesis"
objective: "Demonstrates how to run multiple chains in parallel and synthesize their outputs using LangChain's RunnableParallel."
how_to_run: "Requires LangChain and an OpenAI API key. Run with `python your_script_name.py`."
from_note: "../patterns/parallelization.md"
---

# Parallelization with LangChain: Map and Synthesis

This snippet demonstrates a map-reduce-like pattern in LangChain. It uses `RunnableParallel` to execute two independent chains (`summarize_chain` and `questions_chain`) concurrently on the same input topic. The results are then passed to a final synthesis chain to generate a comprehensive answer.

## Code Example

```python
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
    Synthesize a comprehensive answer."""
    ),
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
```

## How It Works

1.  **Independent Chains**: Two separate chains, `summarize_chain` and `questions_chain`, are defined. Each takes a "topic" as input and performs a different task (summarization and question generation).
2.  **Parallel Execution (`map_chain`)**: `RunnableParallel` is used to create `map_chain`. It takes a dictionary where each value is a runnable. When `map_chain` is invoked with a topic, it runs `summarize_chain` and `questions_chain` in parallel. The `RunnablePassthrough` ensures the original topic is also carried forward.
3.  **Synthesis**: The output of `map_chain` is a dictionary containing the summary, questions, and the original topic. This dictionary is then piped into a `synthesis_prompt` and a final LLM call to generate a single, synthesized response.
4.  **Asynchronous Invocation**: The example uses `ainvoke` to run the chain asynchronously, which is best practice for I/O-bound operations like API calls.