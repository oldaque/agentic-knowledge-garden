---
name: "LangGraph DeepSearch Example"
objective: "Illustrates the creation of an Agent Graph using LangGraph for advanced research and conversational AI, featuring dynamic query generation, web research, and reflective reasoning."
how_to_run: "This is a conceptual code block demonstrating a LangGraph agent. It requires a full LangGraph and Google Gemini setup, including specific node functions (generate_query, web_research, reflection, finalize_answer) and state definitions (OverallState, Configuration) not provided here."
from_note: "../patterns/reasoning-techniques.md"
---

## Explanation

This code demonstrates a sophisticated **multi-step reasoning system** using LangGraph's state graph architecture. The implementation creates a research agent that iteratively refines its search strategy through a cyclical workflow combining query generation, web research, reflection, and answer finalization.

The agent workflow consists of four main nodes:

1. **generate_query**: Creates targeted search queries based on the current research state and previous findings
2. **web_research**: Executes web searches in parallel branches, gathering information from multiple sources
3. **reflection**: Critically evaluates gathered research, identifying gaps or quality issues
4. **finalize_answer**: Synthesizes findings into a comprehensive response

The key innovation is the **reflective reasoning loop**: after web research, the agent reflects on whether the information is sufficient and high-quality. The `evaluate_research` conditional edge determines whether to:
- Continue researching with refined queries (loop back to web_research)
- Finalize the answer (proceed to finalize_answer node)

This architecture implements several advanced reasoning patterns:
- **Iterative refinement**: Multiple research cycles improve answer quality
- **Self-evaluation**: The agent assesses its own progress before committing to an answer
- **Parallel execution**: Web research branches run concurrently for efficiency
- **State-based reasoning**: The OverallState carries context across iterations

The pattern is particularly effective for complex research tasks requiring synthesis from multiple sources, fact verification, or deep domain exploration where initial queries may not yield complete answers.

## Code

```python
# Create our Agent Graph
builder = StateGraph(OverallState, config_schema=Configuration)

# Define the nodes we will cycle between
builder.add_node("generate_query", generate_query)
builder.add_node("web_research", web_research)
builder.add_node("reflection", reflection)
builder.add_node("finalize_answer", finalize_answer)

# Set the entrypoint as `generate_query`
# This means that this node is the first one called
builder.add_edge(START, "generate_query")

# Add conditional edge to continue with search queries in a parallel branch
builder.add_conditional_edges( "generate_query", continue_to_web_research, ["web_research"] )

# Reflect on the web research
builder.add_edge("web_research", "reflection")

# Evaluate the research
builder.add_conditional_edges( "reflection", evaluate_research, ["web_research", "finalize_answer"] )

# Finalize the answer
builder.add_edge("finalize_answer", END)

graph = builder.compile(name="pro-search-agent")
```
