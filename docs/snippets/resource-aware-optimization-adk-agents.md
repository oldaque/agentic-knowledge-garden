---
name: "ADK Agents for Resource-Aware Optimization"
objective: "Demonstrates defining ADK agents with different models (Gemini Pro and Flash) for resource-aware optimization."
how_to_run: "This is a conceptual code block demonstrating agent definition within the Google ADK framework. It is not directly runnable as a standalone script without a full ADK environment setup."
from_note: "../patterns/resource-aware-optimization.md"
---

## Explanation

This code demonstrates **resource-aware optimization** through model selection in Google's ADK framework. The implementation defines two agents using different Gemini model variants, each optimized for different use cases based on the complexity-cost tradeoff.

The two agent configurations represent a common optimization strategy:

1. **GeminiProAgent** (using gemini-2.5-pro):
   - Higher capability model for complex reasoning tasks
   - Better performance on nuanced problems, multi-step reasoning, and domain expertise
   - Higher cost per token and slower inference
   - Suitable for: legal analysis, strategic planning, code generation, complex data analysis

2. **GeminiFlashAgent** (using gemini-2.5-flash):
   - Optimized for speed and cost efficiency
   - Lower cost per token and faster inference
   - Suitable for: simple Q&A, classification, summarization, routine queries

The resource-aware optimization pattern works by:
- **Query classification**: Analyze incoming requests to determine complexity
- **Dynamic routing**: Direct simple queries to Flash, complex queries to Pro
- **Cost management**: Minimize expenses by avoiding over-provisioning (using Pro for Flash-level tasks)
- **Latency optimization**: Use faster models when high capability isn't needed

In production implementations, you would add:
- A router agent or classification function to analyze query complexity
- Token budget tracking and enforcement
- Performance monitoring and model switching logic
- Fallback mechanisms if the simpler model fails
- Cost/performance metrics collection

This pattern can reduce AI costs by 60-80% while maintaining quality for complex queries, as most production workloads contain a mix of simple and complex requests.

## Code

```python
from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm # If using models not directly supported by ADK's default Agent

# Agent using the more expensive Gemini Pro 2.5
gemini_pro_agent = Agent(
    name="GeminiProAgent",
    model="gemini-2.5-pro", # Placeholder for actual model name if different
    description="A highly capable agent for complex queries.",
    instruction="You are an expert assistant for complex problem-solving."
)

# Agent using the less expensive Gemini Flash 2.5
gemini_flash_agent = Agent(
    name="GeminiFlashAgent",
    model="gemini-2.5-flash", # Placeholder for actual model name if different
    description="A fast and efficient agent for simple queries.",
    instruction="You are a quick assistant for straightforward questions."
)
```
