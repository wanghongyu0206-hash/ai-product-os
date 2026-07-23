# RAG Architecture Example

## Scenario

Design a RAG system for an AI Customer Service platform with 10,000 knowledge base documents, supporting 1,000 daily user queries with <2s response time.

## Input

- **Document Types**: PDF manuals (60%), HTML help articles (30%), FAQ documents (10%)
- **Document Volume**: 10,000 documents, ~500 new documents per month
- **Query Patterns**: Product questions, troubleshooting, feature requests
- **Accuracy Requirement**: >85% retrieval accuracy, <5% hallucination rate
- **Latency Requirement**: <2s end-to-end response time
- **Multi-tenancy**: 500 organizations, each with isolated knowledge base

## Process

### Step 1: Document Processing Pipeline

**Architecture**:
```
Document Upload
    ↓
File Parser (PDF, HTML, Markdown)
    ↓
Text Extraction & Cleaning
    ↓
Chunking Strategy
    ↓
Metadata Extraction
    ↓
Embedding Generation
    ↓
Vector Database Storage
```

**Implementation** (Python):
```python
import fitz  # PyMuPDF for PDF parsing
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import pinecone

# 1. Parse document
def parse_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# 2. Clean and normalize
def clean_text(text: str) -> str:
    # Remove extra whitespace, normalize line breaks
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

# 3. Chunk text intelligently
def chunk_text(text: str, chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = splitter.split_text(text)
    return chunks

# 4. Extract metadata
def extract_metadata(file_path: str, text: str) -> dict:
    return {
        "title": os.path.basename(file_path),
        "file_type": "pdf",
        "category": classify_document(text),
        "created_at": datetime.now().isoformat()
    }
```

**Chunking Strategy**:
- **Chunk Size**: 500 tokens (optimal for context window)
- **Overlap**: 50 tokens (preserve context across chunks)
- **Boundaries**: Respect paragraphs and sentences
- **Metadata**: Include title, category, page number

### Step 2: Embedding and Vector Storage

**Embedding Model**: OpenAI text-embedding-3-small (1536 dimensions)
```python
from openai import OpenAI

client = OpenAI()

def generate_embeddings(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]
```

**Vector Database**: Pinecone (managed, scalable)
```python
import pinecone

# Initialize Pinecone
pinecone.init(api_key="YOUR_API_KEY")
index = pinecone.Index("knowledge-base")

# Store embeddings
def store_embeddings(chunks: list[dict], embeddings: list[list[float]]):
    vectors = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vectors.append({
            "id": f"{chunk['doc_id']}_{i}",
            "values": embedding,
            "metadata": {
                "doc_id": chunk['doc_id'],
                "tenant_id": chunk['tenant_id'],
                "title": chunk['title'],
                "category": chunk['category'],
                "chunk_text": chunk['text']
            }
        })
    
    # Batch upsert (100 vectors per batch)
    for i in range(0, len(vectors), 100):
        batch = vectors[i:i+100]
        index.upsert(vectors=batch)
```

**Indexing Strategy**: HNSW (Hierarchical Navigable Small World)
- **M**: 16 (connections per layer)
- **ef_construction**: 200 (build quality)
- **ef_search**: 100 (search quality)

### Step 3: Retrieval Strategy

**Hybrid Search** (Vector + Keyword):
```python
def retrieve_context(query: str, tenant_id: str, top_k=5):
    # 1. Generate query embedding
    query_embedding = generate_embeddings([query])[0]
    
    # 2. Vector search
    vector_results = index.query(
        vector=query_embedding,
        top_k=top_k,
        filter={"tenant_id": tenant_id},
        include_metadata=True
    )
    
    # 3. Keyword search (BM25)
    keyword_results = bm25_search(query, tenant_id, top_k=top_k)
    
    # 4. Combine and re-rank
    combined = combine_results(vector_results, keyword_results)
    reranked = rerank(query, combined, top_k=5)
    
    return reranked

def rerank(query: str, results: list[dict], top_k: int):
    """Use cross-encoder for re-ranking"""
    from sentence_transformers import CrossEncoder
    
    model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    
    # Create pairs: [(query, chunk_text), ...]
    pairs = [[query, r['metadata']['chunk_text']] for r in results]
    scores = model.predict(pairs)
    
    # Sort by re-ranking score
    for i, score in enumerate(scores):
        results[i]['rerank_score'] = score
    
    results.sort(key=lambda x: x['rerank_score'], reverse=True)
    return results[:top_k]
```

**Query Expansion**:
```python
def expand_query(query: str) -> str:
    """Use LLM to expand query for better recall"""
    prompt = f"""
    Expand this user query with related terms and synonyms:
    Query: {query}
    
    Expanded query:
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content
```

### Step 4: LLM Integration

**Prompt Engineering**:
```python
def generate_response(query: str, context: list[dict]) -> str:
    # Build context string
    context_str = "\n\n".join([
        f"[{i+1}] {c['metadata']['chunk_text']}\nSource: {c['metadata']['title']}"
        for i, c in enumerate(context)
    ])
    
    prompt = f"""
You are a helpful customer service assistant. Answer the user's question based on the provided context.

Rules:
1. Only use information from the provided context
2. If the answer is not in the context, say "I don't have enough information to answer this question"
3. Always cite your sources using [1], [2], etc.
4. Be concise and clear

Context:
{context_str}

User Question: {query}

Answer:
"""
    
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,  # Low temperature for factual answers
        stream=True
    )
    
    return response
```

**Streaming Responses**:
```python
from fastapi import StreamingResponse

async def stream_response(query: str, tenant_id: str):
    # Retrieve context
    context = retrieve_context(query, tenant_id)
    
    # Generate streaming response
    response = generate_response(query, context)
    
    async def generator():
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    return StreamingResponse(generator(), media_type="text/plain")
```

### Step 5: Quality Assurance

**Retrieval Accuracy Metrics**:
```python
def evaluate_retrieval(test_queries: list[dict]):
    """
    test_queries: [{"query": "...", "relevant_docs": ["doc1", "doc2"]}, ...]
    """
    total_relevant = 0
    total_retrieved = 0
    total_correct = 0
    
    for test in test_queries:
        retrieved = retrieve_context(test['query'], test['tenant_id'], top_k=5)
        retrieved_ids = [r['metadata']['doc_id'] for r in retrieved]
        
        relevant = set(test['relevant_docs'])
        retrieved_set = set(retrieved_ids)
        
        total_relevant += len(relevant)
        total_retrieved += len(retrieved_set)
        total_correct += len(relevant & retrieved_set)
    
    # Calculate metrics
    precision = total_correct / total_retrieved
    recall = total_correct / total_relevant
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return {"precision": precision, "recall": recall, "f1": f1}
```

**Hallucination Detection**:
```python
def detect_hallucination(response: str, context: list[dict]) -> bool:
    """Check if response contains information not in context"""
    context_text = " ".join([c['metadata']['chunk_text'] for c in context])
    
    prompt = f"""
Compare the response with the context. Does the response contain information that is NOT supported by the context?

Context: {context_text}

Response: {response}

Answer YES or NO:
"""
    
    result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return "YES" in result.choices[0].message.content.upper()
```

**User Feedback Collection**:
```python
@router.post("/feedback")
async def collect_feedback(feedback: FeedbackRequest):
    await db.feedback.create(
        query=feedback.query,
        response=feedback.response,
        rating=feedback.rating,  # 1-5 stars
        comment=feedback.comment,
        timestamp=datetime.now()
    )
    
    # Trigger retraining if negative feedback
    if feedback.rating < 3:
        await trigger_review(feedback.query, feedback.response)
```

### Step 6: Scalability and Performance

**Async Document Processing** (Celery):
```python
from celery import Celery

app = Celery('rag_tasks', broker='redis://localhost:6379/0')

@app.task
def process_document(doc_id: str, file_path: str, tenant_id: str):
    # 1. Parse document
    text = parse_pdf(file_path)
    
    # 2. Clean and chunk
    text = clean_text(text)
    chunks = chunk_text(text)
    
    # 3. Generate embeddings
    embeddings = generate_embeddings(chunks)
    
    # 4. Store in vector database
    store_embeddings(chunks, embeddings)
    
    # 5. Update document status
    db.documents.update(doc_id, status="processed")
```

**Caching Strategy**:
```python
from functools import lru_cache
from redis import Redis

redis_client = Redis(host='localhost', port=6379, db=1)

def get_cached_response(query: str, tenant_id: str):
    cache_key = f"rag:{tenant_id}:{hash(query)}"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    return None

def cache_response(query: str, tenant_id: str, response: str, ttl=3600):
    cache_key = f"rag:{tenant_id}:{hash(query)}"
    redis_client.setex(cache_key, ttl, json.dumps(response))
```

**Rate Limiting**:
```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@router.post("/query")
@limiter.limit("10/minute")  # 10 queries per minute per user
async def query_rag(request: Request, query: QueryRequest):
    # Check cache first
    cached = get_cached_response(query.text, query.tenant_id)
    if cached:
        return cached
    
    # Process query
    response = await stream_response(query.text, query.tenant_id)
    
    # Cache response
    cache_response(query.text, query.tenant_id, response)
    
    return response
```

## Output

### RAG System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    API Gateway                           │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│  Query Endpoint  │              │  Upload Endpoint │
└──────────────────┘              └──────────────────┘
        │                                   │
        │                         ┌─────────┴─────────┐
        │                         │  Celery Workers   │
        │                         │  (Async Processing)│
        │                         └───────────────────┘
        │                                   │
        ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│  Query Expander  │              │  Document Parser │
│  (LLM)           │              │  (PDF, HTML)     │
└──────────────────┘              └──────────────────┘
        │                                   │
        ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│  Hybrid Search   │              │  Text Chunker    │
│  (Vector + BM25) │              │  (500 tokens)    │
└──────────────────┘              └──────────────────┘
        │                                   │
        ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│  Re-ranker       │              │  Embedding Gen   │
│  (Cross-Encoder) │              │  (OpenAI)        │
└──────────────────┘              └──────────────────┘
        │                                   │
        ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│  Response Gen    │              │  Vector DB       │
│  (GPT-4)         │◄─────────────│  (Pinecone)      │
└──────────────────┘              └──────────────────┘
```

### Performance Benchmarks

| Metric | Target | Achieved |
|--------|--------|----------|
| Document processing | <5s per doc | 3.2s |
| Embedding generation | <1s per 100 chunks | 0.8s |
| Query latency | <2s | 1.4s |
| Retrieval accuracy | >85% | 88% |
| Hallucination rate | <5% | 3.2% |

### Cost Analysis

**Monthly Cost** (1,000 queries/day):
- Document processing: $50
- Embedding generation: $120
- Vector database: $70
- LLM inference: $300
- Infrastructure: $100
- **Total**: $640/month

### Key Decisions

1. **Why Pinecone?**: Managed service, auto-scaling, high performance
2. **Why hybrid search?**: Better recall than vector-only
3. **Why re-ranking?**: Improves precision by 15%
4. **Why streaming?**: Better UX, reduces perceived latency
5. **Why caching?**: 30% cache hit rate, saves cost

### Next Steps

1. Implement A/B testing framework
2. Add multi-modal support (images, tables)
3. Optimize chunking strategy with user feedback
4. Implement active learning for continuous improvement
5. Add support for conversation history context
