---
name: "LLM Interaction Monitor (Token Usage)"
objective: "Illustrates a conceptual Python class for tracking token usage in Large Language Model (LLM) interactions, essential for cost management and optimization."
how_to_run: "This is a conceptual Python class. You can run the example usage in a Python environment. For real-world use, integrate with specific LLM API tokenizers."
from_note: "../patterns/evaluation-and-monitoring.md"
---

## Explanation

This code demonstrates a basic token usage monitoring system for LLM interactions. The `LLMInteractionMonitor` class tracks both input (prompt) and output (response) tokens across multiple API calls, which is crucial for cost management and performance optimization.

The current implementation uses a simple word-splitting heuristic as a placeholder for token counting. In production, you should replace this with the actual tokenizer from your LLM provider (e.g., `tiktoken` for OpenAI, or the tokenizer provided by the Gemini/Anthropic/etc. SDK). Different models use different tokenization schemes, so accurate counting requires the model-specific tokenizer.

The example shows recording two interactions and retrieving cumulative token usage. This pattern can be extended to include:
- Per-interaction cost calculation (tokens × price per token)
- Rate limiting based on token budgets
- Performance monitoring (tokens per second)
- Token efficiency metrics (output tokens / input tokens ratio)
- Integration with logging/observability platforms

## Code

```python
# This is conceptual as actual token counting depends on the LLM API
class LLMInteractionMonitor:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record_interaction(self, prompt: str, response: str):
        # In a real scenario, use LLM API's token counter or a tokenizer
        input_tokens = len(prompt.split()) # Placeholder
        output_tokens = len(response.split()) # Placeholder
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        print(f"Recorded interaction: Input tokens={input_tokens}, Output tokens={output_tokens}")

    def get_total_tokens(self):
        return self.total_input_tokens, self.total_output_tokens

# Example usage
monitor = LLMInteractionMonitor()
monitor.record_interaction("What is the capital of France?", "The capital of France is Paris.")
monitor.record_interaction("Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!")
input_t, output_t = monitor.get_total_tokens()
print(f"Total input tokens: {input_t}, Total output tokens: {output_t}")
```
