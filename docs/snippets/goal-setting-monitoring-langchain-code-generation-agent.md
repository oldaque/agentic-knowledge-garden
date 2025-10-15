---
title: "Goal Setting - LangChain Code Generation Agent"
slug: "goal-setting-monitoring-langchain-code-generation-agent"
summary: "Demonstrates iterative code generation with goal setting and monitoring using LangChain, featuring a feedback loop between code generator and critic."
tags: ["langchain", "goal-setting", "code-generation", "feedback-loop", "iterative-refinement"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/goal-setting-and-monitoring.md"
languages: ["python"]
how_to_run: "Requires OPENAI_API_KEY. Run: python goal-setting-monitoring-langchain-code-generation-agent.py"
related_patterns: ["docs/patterns/goal-setting-and-monitoring.md"]
---

## Context

This snippet demonstrates the Goal Setting and Monitoring pattern through an AI coding agent that sets explicit goals, generates code, receives feedback from a critic, and iteratively improves until goals are met. The system uses LLM-based evaluation to determine when defined objectives have been achieved, showcasing how agents can monitor progress toward measurable outcomes through multiple refinement cycles.

## Snippet

```python
# MIT License
# Copyright (c) 2025 Mahtab Syed

import os
import random
import re
from pathlib import Path
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI model
print("Initializing OpenAI LLM (gpt-4o)...")
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY,
)

# --- Utility Functions ---
def generate_prompt(
    use_case: str,
    goals: list[str],
    previous_code: str = "",
    feedback: str = "",
) -> str:
    base_prompt = f"""
You are an AI coding agent. Your job is to write Python code based on the following use case:

Use Case: {use_case}

Your goals are:
{chr(10).join(f"- {g.strip()}" for g in goals)}
"""
    if previous_code:
        base_prompt += f"\nPreviously generated code:\n{previous_code}"
    if feedback:
        base_prompt += f"\nFeedback on previous version:\n{feedback}\n"
    base_prompt += "\nPlease return only the revised Python code. Do not include comments or explanations outside the code."
    return base_prompt

def get_code_feedback(code: str, goals: list[str]) -> str:
    feedback_prompt = f"""
You are a Python code reviewer. A code snippet is shown below. Based on the following goals:

{chr(10).join(f"- {g.strip()}" for g in goals)}

Please critique this code and identify if the goals are met. Mention if improvements are needed for clarity, simplicity, correctness, edge case handling, or test coverage.

Code:
{code}
"""
    return llm.invoke(feedback_prompt)

def goals_met(feedback_text: str, goals: list[str]) -> bool:
    """
    Uses the LLM to evaluate whether the goals have been met based on the feedback text.
    Returns True or False (parsed from LLM output).
    """
    review_prompt = f"""
You are an AI reviewer.

Here are the goals:
{chr(10).join(f"- {g.strip()}" for g in goals)}

Here is the feedback on the code:
{feedback_text}

Based on the feedback above, have the goals been met?

Respond with only one word: True or False.
"""
    response = llm.invoke(review_prompt).content.strip().lower()
    return response == "true"

def clean_code_block(code: str) -> str:
    lines = code.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()

def add_comment_header(code: str, use_case: str) -> str:
    comment = f"# This Python program implements the following use case:\n# {use_case.strip()}\n"
    return comment + "\n" + code

def save_code_to_file(code: str, use_case: str) -> str:
    summary_prompt = (
        f"Summarize the following use case into a single lowercase word or phrase, "
        f"no more than 10 characters, suitable for a Python filename:\n\n{use_case}"
    )
    raw_summary = llm.invoke(summary_prompt).content.strip()
    short_name = re.sub(r"[^a-zA-Z0-9_]", "", raw_summary.replace(" ", "_").lower())[:10]

    random_suffix = str(random.randint(1000, 9999))
    filename = f"{short_name}_{random_suffix}.py"
    filepath = Path.cwd() / filename

    with open(filepath, "w") as f:
        f.write(code)
    return str(filepath)

# --- Main Agent Function ---
def run_code_agent(use_case: str, goals_input: str, max_iterations: int = 5) -> str:
    goals = [g.strip() for g in goals_input.split(",")]

    previous_code = ""
    feedback = ""

    for i in range(max_iterations):
        prompt = generate_prompt(use_case, goals, previous_code, feedback if isinstance(feedback, str) else feedback.content)
        code_response = llm.invoke(prompt)
        raw_code = code_response.content.strip()
        code = clean_code_block(raw_code)

        feedback = get_code_feedback(code, goals)
        feedback_text = feedback.content.strip()

        if goals_met(feedback_text, goals):
            break
        previous_code = code

    final_code = add_comment_header(code, use_case)
    return save_code_to_file(final_code, use_case)

# --- CLI Test Run ---
if __name__ == "__main__":
    use_case_input = "Write code to find BinaryGap of a given positive integer"
    goals_input = "Code simple to understand, Functionally correct, Handles comprehensive edge cases, Takes positive integer input only, prints the results with few examples"
    run_code_agent(use_case_input, goals_input)
```

## Notes

Key implementation details:

- **Goal Definition**: Agent accepts explicit, comma-separated goals as input criteria
- **Iterative Refinement**: Generates code, receives critique, and refines up to max_iterations
- **LLM-based Evaluation**: Uses separate LLM call to determine if goals have been achieved
- **Feedback Loop**: Critic provides specific feedback on clarity, correctness, and edge cases
- **File Management**: Automatically generates filename from use case and saves final code
- **Clean Output**: Strips markdown code fences and adds descriptive header comments
