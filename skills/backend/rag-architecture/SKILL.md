# RAG Architecture Skill

## Goal

Design Retrieval-Augmented Generation (RAG) systems that combine vector search with LLM generation to provide accurate, context-aware AI responses.

## When To Use

- Building knowledge base Q&A systems
- Creating customer support chatbots with document context
- Implementing semantic search with AI summarization
- Designing document ingestion and embedding pipelines
- Optimizing retrieval accuracy and response quality
- Scaling RAG systems for high-traffic applications

## Workflow

### Step 1

Analyze RAG requirements.

Identify:
- Document types and formats (PDF, HTML, Markdown, etc.)
- Document volume and update frequency
- Query patterns and complexity
- Accuracy requirements
- Latency requirements
- Multi-tenancy needs

### Step 2

Design document processing pipeline.

Implement:
- Document ingestion (upload, parsing, extraction)
- Text chunking strategy (size, overlap, boundaries)
- Metadata extraction (title, author, date, category)
- Content cleaning and normalization
- Duplicate detection

### Step 3

Design embedding and vector storage.

Choose:
- Embedding model (OpenAI, Cohere, open-source)
- Vector database (Pinecone, Weaviate, Qdrant, pgvector)
- Embedding dimensions and similarity metric
- Indexing strategy (HNSW, IVF, etc.)
- Hybrid search (vector + keyword)

### Step 4

Design retrieval strategy.

Optimize:
- Top-K retrieval (number of chunks)
- Re-ranking (cross-encoder models)
- Filtering (tenant, category, date)
- Query expansion and rewriting
- Context window management

### Step 5

Design LLM integration.

Configure:
- LLM provider selection (OpenAI, Anthropic, local)
- Prompt engineering (system prompt, context injection)
- Response formatting and citation
- Streaming responses
- Fallback strategies

### Step 6

Design quality assurance.

Implement:
- Retrieval accuracy metrics
- Response quality evaluation
- Hallucination detection
- User feedback collection
- A/B testing framework

### Step 7

Design scalability and performance.

Plan:
- Async document processing
- Batch embedding generation
- Vector database scaling
- Caching strategies (query results, embeddings)
- Rate limiting and quota management

### Step 8

Document RAG architecture.

Create:
- System architecture diagram
- Document processing flow
- Retrieval and generation flow
- Performance benchmarks
- Configuration guide

## Rules

1. Chunk documents intelligently—respect semantic boundaries.
2. Use hybrid search (vector + keyword) for better recall.
3. Always include source citations in responses.
4. Implement re-ranking to improve precision.
5. Monitor retrieval accuracy and hallucination rates.
6. Cache frequent queries to reduce latency and cost.
7. Use streaming responses for better user experience.
8. Test with diverse query types and edge cases.

## Output

- RAG system architecture diagram
- Document processing pipeline design
- Embedding and vector storage configuration
- Retrieval strategy documentation
- LLM integration specification
- Quality assurance plan
- Performance benchmarks
- Configuration and deployment guide

## Quality Criteria

- Document processing is reliable and scalable
- Retrieval accuracy meets target (>80% relevant results)
- Response quality is high (low hallucination rate)
- Latency meets requirements (<2s end-to-end)
- System scales with document volume
- Comprehensive monitoring and logging
- Source citations always included
- Fallback strategies implemented
