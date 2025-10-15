---
title: "Prompt Chaining - LangChain Extraction and Transformation"
slug: "prompt-chaining-langchain-extraction-transformation"
summary: "Demonstrates prompt chaining using LangChain to extract information from unstructured text and transform it into structured JSON format through sequential processing."
tags: ["langchain", "prompt-chaining", "lcel", "extraction", "json"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/prompt-chaining.md"
languages: ["python"]
how_to_run: "Requires OPENAI_API_KEY environment variable. Run: python prompt-chaining-langchain-extraction-transformation.py"
related_patterns: ["docs/patterns/prompt-chaining.md"]
---

## Context

This snippet demonstrates the Prompt Chaining pattern using LangChain Expression Language (LCEL). It shows how to sequentially process information through two linked prompts: first extracting technical specifications from unstructured text, then transforming those specifications into structured JSON format. The pattern uses LangChain's pipe operator to chain prompts together, where the output of one becomes the input to the next.

## Snippet

```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# For better security, load environment variables from a .env file
# from dotenv import load_dotenv
# load_dotenv()
# Make sure your OPENAI_API_KEY is set in the .env file

# Initialize the Language Model (using ChatOpenAI is recommended)
llm = ChatOpenAI(temperature=0)

# --- Prompt 1: Extract Information ---
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n{text_input}"
)

# --- Prompt 2: Transform to JSON ---
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

# --- Build the Chain using LCEL ---
# The StrOutputParser() converts the LLM's message output to a simple string.
extraction_chain = prompt_extract | llm | StrOutputParser()

# The full chain passes the output of the extraction chain into the 'specifications'
# variable for the transformation prompt.
full_chain = (
    {"specifications": extraction_chain}
    | prompt_transform
    | llm
    | StrOutputParser()
)

# --- Run the Chain ---
input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."

# Execute the chain with the input text dictionary.
final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
print(final_result)
```

## Notes

Key implementation details:

- **LCEL Composition**: Uses LangChain's `|` operator to chain two prompts together seamlessly
- **Sequential Processing**: First prompt extracts specifications, second prompt transforms them to JSON
- **Output Parsing**: `StrOutputParser()` converts LLM messages to simple strings for easy downstream processing
- **Data Flow**: The extraction chain's output becomes the input for the transformation step via dictionary mapping
- **Temperature Setting**: Uses `temperature=0` for deterministic, consistent outputs
