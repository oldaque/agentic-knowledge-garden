---
title: "Pattern: Prompt Chaining"
slug: "prompt-chaining"
tags: ["prompt-chaining", "pipeline", "agentic-pattern", "langchain", "workflow"]
themes: ["reasoning/sequencing", "workflow/orchestration"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Break complex goals into sequential prompts where each output feeds the next, keeping agents reliable, interpretable e fáceis de depurar."
relationships:
  snippets:
    - "snippets/prompt-chaining/prompt-chaining-langchain-extraction-transformation.md"
  examples:
    - "examples/prompt-chaining/README.md"
  resources: []
---

### Problem

Agentes costumam falhar quando tentam resolver problemas extensos em um único prompt: o modelo ignora instruções, perde contexto e propaga erros de passos iniciais. O resultado é imprevisível e difícil de diagnosticar.

### Pattern

Prompt Chaining divide o objetivo em etapas curtas e determinísticas. Cada etapa tem um papel explícito, produz um artefato autocontido e passa esse artefato como entrada da etapa seguinte.  
Boas práticas:
- Especificar o papel do modelo em cada etapa para limitar escopo cognitivo.
- Validar o output antes de encadear (ex.: normalizar JSON, checar tokens esperados).
- Injetar ferramentas externas entre etapas conforme necessário (busca, cálculos).

### Trade_offs

- **Pró:** melhor controle, depuração simples e limites de contexto menores por etapa.  
- **Pró:** fácil inserir verificações e correções automáticas entre passos.  
- **Contra:** maior latência total e custo de tokens somados.  
- **Contra:** cadeia longa pode acumular erro se validações forem fracas.

### When_to_use

- Tarefas com múltiplas transformações (extração → análise → geração).  
- Quando é necessário explicar o raciocínio intermediário.  
- Em pipelines que precisam misturar LLM com ferramentas externas entre passos.

### Minimal_example

- Snippet recomendado: [`snippets/prompt-chaining-langchain-extraction-transformation.md`](../snippets/prompt-chaining-langchain-extraction-transformation.md) demonstra extração + transformação usando LangChain.

### Further_reading

- [Livro Agentic Design Patterns — Capítulo 1](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0)
- [LangChain Docs — Sequential Chains](https://python.langchain.com/docs/modules/chains/)

### The Role of Structured Output
The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.

For example, the output from the trend identification step could be formatted as a JSON object:

```json
{
  "trends": [
    {
      "trend_name": "AI-Powered Personalization",
      "supporting_data": "73% of consumers prefer to do business with brands that use personal information to make their shopping experiences more relevant."
    },
    {
      "trend_name": "Sustainable and Ethical Brands",
      "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared to 20% for products without."
    }
  ]
}
```

This structured format ensures that the data is machine-readable and can be precisely parsed and inserted into the next prompt without ambiguity. This practice minimizes errors that can arise from interpreting natural language and is a key component in building robust, multi-step LLM-based systems.

## PRACTICAL APPLICATIONS & USE CASES

Prompt chaining is a versatile pattern applicable in a wide range of scenarios when building agentic systems. Its core utility lies in breaking down complex problems into sequential, manageable steps. Here are several practical applications and use cases:

1.  **Information Processing Workflows:** Many tasks involve processing raw information through multiple transformations. For instance, summarizing a document, extracting key entities, and then using those entities to query a database or generate a report.
2.  **Complex Query Answering:** Answering complex questions that require multiple steps of reasoning or information retrieval is a prime use case.
3.  **Data Extraction and Transformation:** The conversion of unstructured text into a structured format is typically achieved through an iterative process, requiring sequential modifications to improve the accuracy and completeness of the output.
4.  **Content Generation Workflows:** The composition of complex content is a procedural task that is typically decomposed into distinct phases, including initial ideation, structural outlining, drafting, and subsequent revision
5.  **Conversational Agents with State:** Prompt chaining provides a foundational mechanism for preserving conversational continuity.
6.  **Code Generation and Refinement:** The generation of functional code is typically a multi-stage process, requiring a problem to be decomposed into a sequence of discrete logical operations that are executed progressively
7.  **Multimodal and multi-step reasoning:** Analyzing datasets with diverse modalities necessitates breaking down the problem into smaller, prompt-based tasks.

## HANDS-ON CODE EXAMPLE

[Code Example: LangChain Extraction and Transformation Chain](../snippets/prompt-chaining-langchain-extraction-transformation.md)

## CONTEXT ENGINEERING AND PROMPT ENGINEERING

Context Engineering (see Fig.1) is the systematic discipline of designing, constructing, and delivering a complete informational environment to an AI model prior to token generation. This methodology asserts that the quality of a model's output is less dependent on the model's architecture itself and more on the richness of the context provided.


## AT A GLANCE

**What:** Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues.

**Why:** Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller, interconnected sub-tasks.

**Rule of thumb:** Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building Agentic systems that need to perform multi-step reasoning and maintain state.

### Visual summary


## KEY TAKEAWAYS

*   Prompt Chaining breaks down complex tasks into a sequence of smaller, focused steps. This is occasionally known as the Pipeline pattern.
*   Each step in a chain involves an LLM call or processing logic, using the output of the previous step as input.
*   This pattern improves the reliability and manageability of complex interactions with language models.
*   Frameworks like LangChain/LangGraph, and Google ADK provide robust tools to define, manage, and execute these multi-step sequences.

## CONCLUSION

By deconstructing complex problems into a sequence of simpler, more manageable sub-tasks, prompt chaining provides a robust framework for guiding large language models. This "divide-and-conquer" strategy significantly enhances the reliability and control of the output by focusing the model on one specific operation at a time.

## REFERENCES

1.  [LangChain Documentation on LCEL](https://python.langchain.com/v0.2/docs/core_modules/expression_language/)
2.  [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
3.  [Prompt Engineering Guide - Chaining Prompts](https://www.promptingguide.ai/techniques/chaining)
4.  [OpenAI API Documentation (General Prompting Concepts)](https://platform.openai.com/docs/guides/gpt/prompting)
5.  [Crew AI Documentation (Tasks and Processes)](https://docs.crewai.com/)
6.  [Google AI for Developers (Prompting Guides)](https://cloud.google.com/discover/what-is-prompt-engineering?hl=en)
7.  [Vertex Prompt Optimizer](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer)
