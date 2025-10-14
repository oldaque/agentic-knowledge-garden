---
name: "Knowledge Retrieval (RAG) with ADK and Vertex AI"
objective: "Demonstrates how to use Vertex AI for RAG with the ADK framework."
how_to_run: "Requires Google ADK and a configured Vertex AI RAG Corpus. Run as part of an ADK agent."
from_note: "../patterns/knowledge-retrieval-rag.md"
---

# Knowledge Retrieval with ADK and Vertex AI

This snippet shows how to configure a `VertexAiRagMemoryService` to connect to a Vertex AI RAG corpus for retrieval-augmented generation.

## Code Example

```python
# Import the necessary VertexAiRagMemoryService class from the google.adk.memory module.
from google.adk.memory import VertexAiRagMemoryService

RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id"
# Define an optional parameter for the number of top similar results to retrieve.
# This controls how many relevant document chunks the RAG service will return.
SIMILARITY_TOP_K = 5
# Define an optional parameter for the vector distance threshold.
# This threshold determines the maximum semantic distance allowed for retrieved results;
# results with a distance greater than this value might be filtered out.
VECTOR_DISTANCE_THRESHOLD = 0.7

# Initialize an instance of VertexAiRagMemoryService.
# This sets up the connection to your Vertex AI RAG Corpus.
# - rag_corpus: Specifies the unique identifier for your RAG Corpus.
# - similarity_top_k: Sets the maximum number of similar results to fetch.
# - vector_distance_threshold: Defines the similarity threshold for filtering results.
memory_service = VertexAiRagMemoryService(
    rag_corpus=RAG_CORPUS_RESOURCE_NAME,
    similarity_top_k=SIMILARITY_TOP_K,
    vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD
)
```

## How It Works

- The `VertexAiRagMemoryService` is imported from the ADK library.
- The resource name for the Vertex AI RAG Corpus is defined.
- Parameters like `SIMILARITY_TOP_K` and `VECTOR_DISTANCE_THRESHOLD` are set to control the retrieval process.
- The `VertexAiRagMemoryService` is initialized with the corpus details, making it ready to be used by an ADK agent for memory and retrieval.
