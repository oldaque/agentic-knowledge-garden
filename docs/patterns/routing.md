# Chapter 2: Routing

## ROUTING PATTERN OVERVIEW

While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:

*   **LLM-based Routing:** The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination.
*   **Embedding-based Routing:** The input query can be converted into a vector embedding. This embedding is then compared to embeddings representing different routes or capabilities.
*   **Rule-based Routing:** This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input.
*   **Machine Learning Model-Based Routing:** It employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task.

## PRACTICAL APPLICATIONS & USE CASES

The routing pattern is a critical control mechanism in the design of adaptive agentic systems, enabling them to dynamically alter their execution path in response to variable inputs and internal states.

- **Human-Computer Interaction:** In virtual assistants or AI tutors, routing is used to interpret user intent and select the appropriate action or module.
- **Data and Document Processing:** It acts as a classification and distribution function, directing incoming data like emails or tickets to the correct workflow.
- **Multi-Agent/Tool Systems:** Routing serves as a high-level dispatcher, assigning tasks to the most suitable specialized agent or tool based on the current objective.

## HANDS-ON CODE EXAMPLE (LANGCHAIN)

This example demonstrates a simple coordinator that routes user requests to different sub-agent handlers based on the request's intent.

[Code Example: LangChain Coordinator Router](../../snippets/routing-langchain-coordinator-router.py)

## HANDS-ON CODE EXAMPLE (GOOGLE ADK)

This example shows routing within the Google Agent Development Kit (ADK) by defining a set of "tools" and letting the framework's logic route the user's intent to the correct function.

[Code Example: Google ADK Coordinator with Sub-Agents](../../snippets/routing-google-adk-coordinator-subagents.py)

## AT A GLANCE

**What:** Agentic systems need to handle a variety of inputs that can't be managed by a single, linear process. A rigid workflow lacks the ability to make decisions based on context.

**Why:** The Routing pattern introduces conditional logic. It enables the agent to first analyze an incoming query to determine its intent and then dynamically direct the flow of control to the most appropriate specialized tool, function, or sub-agent.

**Rule of Thumb:** Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user's input or the current state.

## VISUAL SUMMARY

![Fig.1: Router pattern, using an LLM as a Router](placeholder_for_fig1.png)

## KEY TAKEAWAYS

*   Routing enables agents to make dynamic decisions about the next step in a workflow.
*   It allows agents to handle diverse inputs and adapt their behavior, moving beyond linear execution.
*   Routing logic can be implemented using LLMs, rule-based systems, or embedding similarity.
*   Frameworks like LangGraph and Google ADK provide structured ways to define and manage routing.

## CONCLUSION

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. It empowers agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools. Mastering this pattern is essential for creating versatile and robust agentic applications that can handle the variability of real-world tasks.

## REFERENCES

1.  [LangGraph Documentation](https://www.langchain.com/)
2.  [Google Agent Developer Kit Documentation](https://google.github.io/adk-docs/)
