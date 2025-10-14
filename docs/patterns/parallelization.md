---
title: "Chapter 3: Parallelization"
slug: "parallelization"
tags: ["parallelization", "concurrent", "performance", "agentic-pattern", "langchain", "google-adk"]
source:
  type: "book"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1XVMp4RcRkoUJTVbrP2foWZX703CUJpWkrhyFU2cfUOA/edit?tab=t.0"
status: "stable"
last_update: "2025-10-13"
summary: "Pattern for executing independent tasks concurrently to improve performance and reduce overall execution time in agentic systems."
---

# Chapter 3: Parallelization

## PARALLELIZATION PATTERN OVERVIEW

Parallelization involves executing multiple components, such as LLM calls, tool usages, or even entire sub-agents, concurrently. Instead of waiting for one step to complete before starting the next, parallel execution allows independent tasks to run at the same time, significantly reducing the overall execution time for tasks that can be broken down into independent parts.

This pattern is vital for improving the efficiency and responsiveness of agentic systems, especially when dealing with tasks that involve multiple independent lookups, computations, or interactions with external services.

![Fig.1. Example of parallelization with sub-agents](placeholder_for_fig1)

Frameworks like LangChain, LangGraph, and Google ADK provide mechanisms for parallel execution.

## PRACTICAL APPLICATIONS & USE CASES

- **Information Gathering and Research:** Collecting information from multiple sources (news, stock data, social media) simultaneously.
- **Data Processing and Analysis:** Running different analyses (sentiment, keyword extraction) on data segments concurrently.
- **Multi-API or Tool Interaction:** Calling multiple independent APIs (flights, hotels, events) at the same time.
- **Content Generation:** Generating different parts of a complex piece of content (subject line, body, CTA) in parallel.
- **Validation and Verification:** Performing multiple independent checks (email format, phone number) concurrently.

## HANDS-ON CODE EXAMPLE (LANGCHAIN)

This example uses LangChain Expression Language (LCEL) to run multiple chains in parallel and then synthesize their results.

[Code Example: LangChain Parallel Map-Synthesis Chain](../snippets/parallelization-langchain-map-synthesis-chain.py)

## HANDS-ON CODE EXAMPLE (GOOGLE ADK)

This example uses `ParallelAgent` and `SequentialAgent` from the Google ADK to run researcher agents concurrently and then merge their findings.

[Code Example: Google ADK Parallel Research and Synthesis](../snippets/parallelization-google-adk-research-synthesis.py)

## AT A GLANCE

**What:** Purely sequential execution is inefficient for workflows with independent sub-tasks, causing latency, especially with I/O operations like API calls.

**Why:** The Parallelization pattern enables the simultaneous execution of independent tasks, drastically reducing total processing time.

**Rule of thumb:** Use this pattern when a workflow contains multiple independent operations that can run simultaneously, such as fetching data from several APIs or processing different chunks of data.

## VISUAL SUMMARY

![Fig.2: Parallelization design pattern](placeholder_for_fig2)

## KEY TAKEAWAYS

*   Parallelization executes independent tasks concurrently to improve efficiency.
*   It is especially useful for tasks involving I/O waits (e.g., API calls).
*   Frameworks like LangChain (`RunnableParallel`) and Google ADK (`ParallelAgent`) provide built-in support for this pattern.

## CONCLUSION

The parallelization pattern is a method for optimizing computational workflows by concurrently executing independent sub-tasks. By integrating parallel processing with sequential (chaining) and conditional (routing) control flows, it becomes possible to construct sophisticated, high-performance computational systems.

## REFERENCES

1.  [LangChain Expression Language (LCEL) Documentation (Parallelism)](https://python.langchain.com/docs/concepts/lcel/)
2.  [Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems)](https://google.github.io/adk-docs/agents/multi-agents/)
3.  [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
