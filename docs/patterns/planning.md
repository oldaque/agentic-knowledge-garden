---
title: "Chapter 6: Planning"
slug: "planning"
tags: ["planning", "strategy", "workflow", "agentic-pattern", "crewai", "openai"]
source:
  type: "book"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/18vvNESEwHnVUREzIipuaDNCnNAREGqEfy9MQYC9wb4o/edit?usp=sharing"
status: "stable"
last_update: "2025-10-13"
summary: "Pattern for enabling agents to create sequential workflows and break down complex goals into actionable steps."
---

# Chapter 6: Planning

## PLANNING PATTERN OVERVIEW

Intelligent behavior often involves more than just reacting to the immediate input. It requires foresight, breaking down complex tasks into smaller, manageable steps, and strategizing how to achieve a desired outcome. This is where the Planning pattern comes into play. At its core, planning is the ability for an agent or a system of agents to formulate a sequence of actions to move from an initial state towards a goal state.

In the context of AI, a planning agent acts as a specialist to whom you delegate a complex goal. It understands the initial state and the goal state, then discovers the optimal sequence of actions to connect them. The plan is not known in advance; it is created in response to the request.

A hallmark of this process is adaptability. An initial plan is merely a starting point, not a rigid script. The agent's real power is its ability to incorporate new information and steer the project around obstacles.

However, there's a trade-off between flexibility and predictability. Dynamic planning is a specific tool, not a universal solution. When a problem's solution is well-understood and repeatable, a predetermined, fixed workflow is more effective. The decision to use a planning agent versus a simple task-execution agent hinges on a single question: does the "how" need to be discovered, or is it already known?

## PRACTICAL APPLICATIONS & USE CASES

-   **Procedural Task Automation:** Orchestrating complex workflows like new employee onboarding.
-   **Robotics and Autonomous Navigation:** Generating paths or action sequences for physical or virtual entities.
-   **Structured Information Synthesis:** Formulating plans for research reports, including information gathering, summarization, and structuring.
-   **Customer Support:** Creating systematic plans for diagnosis, solution implementation, and escalation in multi-step problem resolution.

## HANDS-ON CODE EXAMPLE (CREW AI)

This section demonstrates an implementation of the Planner pattern using the Crew AI framework, where an agent first formulates a multi-step plan and then executes it.

[Code Example: CrewAI Planner-Writer Agent](../snippets/planning-crewai-planner-writer-agent.md)

## GOOGLE DEEPRESEARCH

Google Gemini DeepResearch is an agent-based system designed for autonomous information retrieval and synthesis. It functions through a multi-step agentic pipeline that dynamically and iteratively queries Google Search to systematically explore complex topics. The system is engineered to process a large corpus of web-based sources, evaluate the collected data for relevance and knowledge gaps, and perform subsequent searches to address them. The final output consolidates the vetted information into a structured, multi-page summary with citations to the original sources.


## OPENAI DEEP RESEARCH API

The OpenAI Deep Research API is a specialized tool designed to automate complex research tasks. It utilizes an advanced, agentic model that can independently reason, plan, and synthesize information from real-world sources. It takes a high-level query and autonomously breaks it down into sub-questions, performs web searches using its built-in tools, and delivers a structured, citation-rich final report.

[Code Example: OpenAI Deep Research API](../snippets/planning-openai-deep-research-api.md)

## AT A GLANCE

**What:** Complex problems often cannot be solved with a single action and require foresight. Without a structured approach, an agentic system struggles to handle multifaceted requests.

**Why:** The Planning pattern offers a standardized solution by having an agentic system first create a coherent plan to address a goal. It involves decomposing a high-level objective into a sequence of smaller, actionable steps or sub-goals.

**Rule of thumb:** Use this pattern when a user's request is too complex to be handled by a single action or tool. It is ideal for automating multi-step processes, such as generating a detailed research report, onboarding a new employee, or executing a competitive analysis.

## VISUAL SUMMARY


## KEY TAKEAWAYS

*   Planning enables agents to break down complex goals into actionable, sequential steps.
*   It is essential for handling multi-step tasks, workflow automation, and navigating complex environments.
*   LLMs can perform planning by generating step-by-step approaches based on task descriptions.
*   Explicitly prompting or designing tasks to require planning steps encourages this behavior in agent frameworks.
*   Google Deep Research is an agent analyzing on our behalf sources obtained using Google Search as a tool. It reflects, plans, and executes.

## CONCLUSION

The Planning pattern is a foundational component that elevates agentic systems from simple reactive responders to strategic, goal-oriented executors. Modern large language models provide the core capability for this, autonomously decomposing high-level objectives into coherent, actionable steps. This pattern scales from straightforward, sequential task execution, as demonstrated by the CrewAI agent creating and following a writing plan, to more complex and dynamic systems. The Google DeepResearch agent exemplifies this advanced application, creating iterative research plans that adapt and evolve based on continuous information gathering.

## REFERENCES

1.  [Google DeepResearch (Gemini Feature)](https://gemini.google.com)
2.  [OpenAI, Introducing deep research](https://openai.com/index/introducing-deep-research/)
3.  [Perplexity, Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
