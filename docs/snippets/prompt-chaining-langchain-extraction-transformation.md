---
name: "Prompt Chaining - LangChain Extraction and Transformation"
objective: "Demonstrates prompt chaining using LangChain to extract information and transform it to JSON format sequentially."
how_to_run: "Requires OPENAI_API_KEY environment variable. Run: python prompt-chaining-langchain-extraction-transformation.py"
from_note: "../patterns/prompt-chaining.md"
---

# Prompt Chaining with LangChain: Extraction and Transformation

This code example demonstrates the Prompt Chaining pattern using LangChain Expression Language (LCEL) to sequentially process information through two linked prompts.

## Code Example

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

## Explanation

This example shows how prompt chaining works by:

1. **First Prompt Chain**: Extracts technical specifications from unstructured text
2. **Second Prompt Chain**: Transforms the extracted specifications into structured JSON format
3. **LCEL Composition**: Uses LangChain's `|` operator to chain the two prompts together

The output of the extraction step becomes the input for the transformation step, creating a sequential processing pipeline.
