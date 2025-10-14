# Chapter 8: Memory Management

## Introduction to Memory Management in Agents
Effective memory management is crucial for agents to retain information, make informed decisions, maintain conversational context, and improve over time.

## Types of Memory
1.  **Short-Term Memory (Contextual Memory)**:
    *   Holds information currently being processed or recently accessed.
    *   Primarily exists within the LLM's context window, including recent messages, tool usage, and reflections.
    *   Has limited capacity and is ephemeral, lost once the session concludes.
2.  **Long-Term Memory (Persistent Memory)**:
    *   A repository for information agents need to retain across various interactions, tasks, or extended periods.
    *   Typically stored outside the agent's immediate processing environment (e.g., databases, knowledge graphs, vector databases).
    *   Enables retrieval based on semantic similarity (semantic search).

## Practical Applications & Use Cases
Memory management is vital for agents to surpass basic question-answering. Applications include:
*   Chatbots and Conversational AI (maintaining flow, recalling preferences).
*   Task-Oriented Agents (tracking steps, progress).
*   Personalized Experiences (storing user preferences, behaviors).
*   Learning and Improvement (refining performance from past interactions).
*   Information Retrieval (RAG - accessing knowledge bases).
*   Autonomous Systems (maps, routes, learned behaviors).

## Memory Management in Google Agent Developer Kit (ADK)
ADK structures context management through:
*   **Session**: An individual chat thread logging messages (Events) and storing temporary data (State). Managed by `SessionService` (e.g., `InMemorySessionService`, `DatabaseSessionService`, `VertexAiSessionService`).
*   **State (`session.state`)**: Data stored within a Session, relevant only to the current chat thread. Operates as a dictionary with key-value pairs. Updates should occur via `output_key` on `LlmAgent` or `EventActions.state_delta` when appending events, not direct modification.
*   **Memory (`MemoryService`)**: A searchable repository for long-term knowledge from past chats or external sources. Managed by `MemoryService` (e.g., `InMemoryMemoryService`, `VertexAiRagMemoryService`). Primary functions are `add_session_to_memory` and `search_memory`.

## Memory Management in LangChain and LangGraph
*   **Short-Term Memory**: Thread-scoped, tracking ongoing conversation within a single session.
    *   `ChatMessageHistory`: Manual control over conversation history.
    *   `ConversationBufferMemory`: Automated integration into chains, making history available to prompts. Can return history as a formatted string or a list of message objects.
*   **Long-Term Memory**: Stores user-specific or application-level data across sessions, shared between conversational threads.
    *   **Semantic Memory**: Remembering facts (e.g., user preferences, domain knowledge).
    *   **Episodic Memory**: Remembering experiences (e.g., how to accomplish a task, often via few-shot examples).
    *   **Procedural Memory**: Remembering rules (agent's core instructions, behaviors, often updated via "Reflection").
    *   LangGraph stores long-term memories as JSON documents in a `BaseStore` (e.g., `InMemoryStore`), organized by namespaces and keys.

## Vertex Memory Bank
A managed service in Vertex AI Agent Engine providing persistent, long-term memory. It uses Gemini models to asynchronously analyze conversation histories, extract key facts, and user preferences, storing them by defined scope (e.g., user ID). It integrates seamlessly with Google ADK and supports other frameworks via direct API calls.

## Key Takeaways
*   Memory is crucial for agents to track, learn, and personalize interactions.
*   Agents require both short-term (contextual, temporary) and long-term (persistent, searchable) memory.
*   Short-term memory is limited by the LLM's context window; long-term memory uses external storage like vector databases.
*   Frameworks like ADK provide specific components: `Session` (chat thread), `State` (temporary chat data), and `MemoryService` (searchable long-term knowledge).
*   ADK's `SessionService` manages the lifecycle of a chat session, and `session.state` is a dictionary for temporary data, updated via `EventActions.state_delta` or `output_key`.
*   LangChain offers `ConversationBufferMemory` for short-term context, while LangGraph enables advanced long-term memory (semantic, episodic, procedural) using stores.
*   Vertex Memory Bank offers a managed service for persistent, long-term memory, integrating with ADK, LangGraph, and CrewAI.
