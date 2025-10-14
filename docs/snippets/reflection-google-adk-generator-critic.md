---
name: "Reflection with ADK: Generator and Critic"
objective: "Demonstrates a generator-critic pattern using ADK's SequentialAgent, where one agent generates content and another critiques it."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/reflection.md"
---

# Reflection with ADK: Generator and Critic

This snippet implements a generator-critic (or "reflection") pattern using the Google ADK. A `generator` agent writes a draft, and a `reviewer` agent critiques it. A `SequentialAgent` orchestrates the process, ensuring the critic runs after the generator.

## Code Example

```python
from google.adk.agents import SequentialAgent, LlmAgent

# The first agent generates the initial draft.
generator = LlmAgent(
    name="DraftWriter",
    description="Generates initial draft content on a given subject.",
    instruction="Write a short, informative paragraph about the user's subject.",
    output_key="draft_text" # The output is saved to this state key.
)

# The second agent critiques the draft from the first agent.
reviewer = LlmAgent(
    name="FactChecker",
    description="Reviews a given text for factual accuracy and provides a structured critique.",
    instruction="""
    You are a meticulous fact-checker.
    1. Read the text provided in the state key 'draft_text'.
    2. Carefully verify the factual accuracy of all claims.
    3. Your final output must be a dictionary containing two keys:
       - "status": A string, either "ACCURATE" or "INACCURATE".
       - "reasoning": A string providing a clear explanation for your status, citing specific issues if any are found.
    """,
    output_key="review_output" # The structured dictionary is saved here.
)

# The SequentialAgent ensures the generator runs before the reviewer.
review_pipeline = SequentialAgent(
    name="WriteAndReview_Pipeline",
    sub_agents=[generator, reviewer]
)

# Execution Flow:
# 1. generator runs -> saves its paragraph to state['draft_text'].
# 2. reviewer runs -> reads state['draft_text'] and saves its dictionary output to state['review_output'].
```

## How It Works

1.  **Generator Agent**: The `generator` agent is a standard `LlmAgent` tasked with writing a draft. Its output is stored in the session state under the key `draft_text`.
2.  **Critic Agent**: The `reviewer` agent is another `LlmAgent`. Its instructions are carefully crafted to make it act as a critic. It is told to read the text from the `draft_text` state key and produce a structured dictionary with a status and reasoning. Its output is saved to the `review_output` key.
3.  **Sequential Pipeline**: A `SequentialAgent` is used to ensure the agents run in the correct order. The `generator` runs first, followed by the `reviewer`.
4.  **State Management**: The session state is used as the communication channel between the two agents. The generator writes to the state, and the reviewer reads from it. This loose coupling is a key feature of the ADK.