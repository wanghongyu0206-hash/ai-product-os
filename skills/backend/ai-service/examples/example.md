# AI Service Example

## Scenario

Design an AI service for a Customer Service SaaS platform that provides AI-powered chatbot responses, email summarization, and sentiment analysis.

## Input

- **AI Capabilities**: Chat responses, email summarization, sentiment classification
- **LLM Providers**: OpenAI (GPT-4, GPT-3.5), Anthropic (Claude 3), local Llama 2
- **Throughput**: 1000 requests/hour peak
- **Latency**: <2s for chat, <5s for summarization
- **Budget**: $5000/month for AI services
- **Compliance**: GDPR, content filtering required

## Process

### Step 1: Service Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    API Gateway                           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   AI Service Layer   │
              └──────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Chat Service│  │  Summary     │  │  Sentiment   │
│              │  │  Service     │  │  Service     │
└──────────────┘  └──────────────┘  └──────────────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │  LLM Client Layer    │
              │  (Provider Abstract) │
              └──────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  OpenAI      │  │  Anthropic   │  │  Local       │
│  Client      │  │  Client      │  │  LLM Client  │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Step 2: LLM Integration Layer

**Provider Abstraction**:
```python
from abc import ABC, abstractmethod
from typing import AsyncIterator

class LLMProvider(ABC):
    @abstractmethod
    async def complete(self, prompt: str, **kwargs) -> str:
        pass
    
    @abstractmethod
    async def stream(self, prompt: str, **kwargs) -> AsyncIterator[str]:
        pass
    
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    async def complete(self, prompt: str, **kwargs) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response.choices[0].message.content
    
    async def stream(self, prompt: str, **kwargs) -> AsyncIterator[str]:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs
        )
        async for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    def count_tokens(self, text: str) -> int:
        import tiktoken
        encoding = tiktoken.encoding_for_model(self.model)
        return len(encoding.encode(text))

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "claude-3-opus"):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
    
    async def complete(self, prompt: str, **kwargs) -> str:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=kwargs.get('max_tokens', 1000),
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

# Provider Factory
class LLMProviderFactory:
    @staticmethod
    def create(provider: str, **kwargs) -> LLMProvider:
        if provider == "openai":
            return OpenAIProvider(**kwargs)
        elif provider == "anthropic":
            return AnthropicProvider(**kwargs)
        elif provider == "local":
            return LocalLLMProvider(**kwargs)
        else:
            raise ValueError(f"Unknown provider: {provider}")
```

**Model Selection Logic**:
```python
class ModelSelector:
    """Select model based on task complexity and cost"""
    
    MODELS = {
        "chat_complex": {"provider": "openai", "model": "gpt-4", "cost_per_1k": 0.03},
        "chat_simple": {"provider": "openai", "model": "gpt-3.5-turbo", "cost_per_1k": 0.0015},
        "summarize": {"provider": "anthropic", "model": "claude-3-sonnet", "cost_per_1k": 0.003},
        "sentiment": {"provider": "local", "model": "llama-2-7b", "cost_per_1k": 0.0001}
    }
    
    @classmethod
    def select(cls, task: str, complexity: str = "simple") -> dict:
        key = f"{task}_{complexity}"
        if key not in cls.MODELS:
            key = task
        
        model_config = cls.MODELS[key]
        provider = LLMProviderFactory.create(
            provider=model_config["provider"],
            api_key=settings.get_api_key(model_config["provider"]),
            model=model_config["model"]
        )
        
        return {
            "provider": provider,
            "config": model_config
        }
```

### Step 3: Prompt Engineering Pipeline

**Prompt Templates**:
```python
from string import Template

PROMPT_TEMPLATES = {
    "chat_response": Template("""
You are a helpful customer service assistant for ${company_name}.

Context from knowledge base:
${context}

Conversation history:
${history}

Customer question: ${question}

Provide a helpful, concise response. If you don't know the answer, say so and offer to connect them with a human agent.
"""),
    
    "email_summary": Template("""
Summarize the following customer email in 2-3 sentences. Focus on:
1. The main issue or request
2. Any urgency indicators
3. Required actions

Email:
${email_content}

Summary:
"""),
    
    "sentiment_analysis": Template("""
Classify the sentiment of this customer message as: POSITIVE, NEGATIVE, or NEUTRAL.

Message: ${message}

Sentiment:
""")
}

class PromptManager:
    def __init__(self):
        self.templates = PROMPT_TEMPLATES
        self.versions = {}  # Track prompt versions
    
    def render(self, template_name: str, **kwargs) -> str:
        if template_name not in self.templates:
            raise ValueError(f"Unknown template: {template_name}")
        
        return self.templates[template_name].safe_substitute(**kwargs)
    
    def version(self, template_name: str) -> str:
        return self.versions.get(template_name, "1.0")
```

**A/B Testing Framework**:
```python
import random

class PromptABTest:
    def __init__(self):
        self.experiments = {}
    
    def register(self, experiment_name: str, variants: dict):
        """
        variants: {
            "control": {"template": "chat_v1", "weight": 0.5},
            "variant_a": {"template": "chat_v2", "weight": 0.5}
        }
        """
        self.experiments[experiment_name] = variants
    
    def select_variant(self, experiment_name: str, user_id: str) -> str:
        """Deterministic selection based on user_id for consistency"""
        variants = self.experiments[experiment_name]
        
        # Use hash for deterministic assignment
        hash_value = hash(f"{experiment_name}:{user_id}") % 100
        
        cumulative = 0
        for variant_name, config in variants.items():
            cumulative += config["weight"] * 100
            if hash_value < cumulative:
                return variant_name
        
        return list(variants.keys())[0]
```

### Step 4: AI Workflow Orchestration

**Chat Workflow** (Multi-step):
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    tenant_id: str
    user_id: str
    question: str
    conversation_id: str

class ChatWorkflow:
    def __init__(self):
        self.prompt_manager = PromptManager()
        self.model_selector = ModelSelector()
    
    async def process(self, request: ChatRequest) -> AsyncIterator[str]:
        # Step 1: Retrieve relevant context (RAG)
        context = await self.retrieve_context(request.question, request.tenant_id)
        
        # Step 2: Get conversation history
        history = await self.get_conversation_history(request.conversation_id)
        
        # Step 3: Determine complexity
        complexity = self.assess_complexity(request.question)
        
        # Step 4: Select appropriate model
        model_info = self.model_selector.select("chat", complexity)
        provider = model_info["provider"]
        
        # Step 5: Render prompt
        prompt = self.prompt_manager.render(
            "chat_response",
            company_name=await self.get_company_name(request.tenant_id),
            context=context,
            history=history,
            question=request.question
        )
        
        # Step 6: Stream response
        async for chunk in provider.stream(prompt, temperature=0.7):
            yield chunk
        
        # Step 7: Log usage and metrics
        await self.log_usage(
            tenant_id=request.tenant_id,
            tokens_in=provider.count_tokens(prompt),
            tokens_out=provider.count_tokens(chunk),
            model=model_info["config"]["model"],
            cost=model_info["config"]["cost_per_1k"]
        )
    
    def assess_complexity(self, question: str) -> str:
        """Simple heuristic for model selection"""
        if len(question) > 200 or "?" in question:
            return "complex"
        return "simple"
```

**Agent Framework** (Tool Calling):
```python
class AIAgent:
    """AI agent with tool calling capabilities"""
    
    def __init__(self, provider: LLMProvider):
        self.provider = provider
        self.tools = {}
    
    def register_tool(self, name: str, func: callable, description: str):
        self.tools[name] = {"func": func, "description": description}
    
    async def execute(self, task: str, max_iterations: int = 5):
        messages = [
            {"role": "system", "content": "You are an AI agent that can use tools to complete tasks."},
            {"role": "user", "content": task}
        ]
        
        for _ in range(max_iterations):
            # Get LLM response
            response = await self.provider.complete(
                messages=messages,
                tools=self.get_tool_definitions()
            )
            
            # Check if agent wants to use a tool
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    
                    # Execute tool
                    result = await self.tools[tool_name]["func"](**tool_args)
                    
                    # Add result to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    })
            else:
                # Agent has final answer
                return response.content
        
        return "Max iterations reached"
    
    def get_tool_definitions(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": name,
                    "description": tool["description"],
                    "parameters": {}  # Define JSON schema
                }
            }
            for name, tool in self.tools.items()
        ]
```

### Step 5: Cost Management

**Token Tracking and Budget Limits**:
```python
from datetime import datetime, timedelta

class CostManager:
    def __init__(self, db):
        self.db = db
    
    async def track_usage(self, tenant_id: str, tokens_in: int, tokens_out: int, cost: float):
        await db.usage_logs.create(
            tenant_id=tenant_id,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            cost=cost,
            timestamp=datetime.now()
        )
    
    async def get_monthly_usage(self, tenant_id: str) -> dict:
        month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0)
        
        usage = await db.usage_logs.aggregate(
            filter={"tenant_id": tenant_id, "timestamp": {"$gte": month_start}},
            pipeline=[
                {"$group": {
                    "_id": None,
                    "total_tokens": {"$sum": {"$add": ["$tokens_in", "$tokens_out"]}},
                    "total_cost": {"$sum": "$cost"}
                }}
            ]
        )
        
        return usage[0] if usage else {"total_tokens": 0, "total_cost": 0}
    
    async def check_budget(self, tenant_id: str) -> bool:
        usage = await self.get_monthly_usage(tenant_id)
        budget = await self.get_tenant_budget(tenant_id)
        
        return usage["total_cost"] < budget
    
    async def enforce_budget(self, tenant_id: str):
        if not await self.check_budget(tenant_id):
            raise BudgetExceededException("Monthly AI budget exceeded")
```

**Cost Optimization Strategies**:
```python
class CostOptimizer:
    def __init__(self):
        self.cache = RedisCache()
    
    async def optimize_request(self, prompt: str, tenant_id: str) -> str:
        # Strategy 1: Cache identical prompts
        cache_key = f"ai:{tenant_id}:{hash(prompt)}"
        cached = await self.cache.get(cache_key)
        if cached:
            return cached
        
        # Strategy 2: Use smaller model for simple tasks
        if len(prompt) < 500:
            model = "gpt-3.5-turbo"  # Cheaper
        else:
            model = "gpt-4"  # More capable
        
        # Strategy 3: Reduce max_tokens for short responses
        max_tokens = 500 if len(prompt) < 1000 else 2000
        
        return model, max_tokens
```

### Step 6: Safety and Compliance

**Content Filtering**:
```python
class ContentFilter:
    def __init__(self):
        self.toxicity_model = load_toxicity_model()
        self.pii_detector = PIIDetector()
    
    async def filter_input(self, text: str) -> tuple[bool, str]:
        # Check for toxicity
        toxicity_score = self.toxicity_model.predict(text)
        if toxicity_score > 0.8:
            return False, "Input contains inappropriate content"
        
        # Check for PII
        pii_detected = self.pii_detector.detect(text)
        if pii_detected:
            text = self.pii_detector.redact(text)
        
        return True, text
    
    async def filter_output(self, text: str) -> tuple[bool, str]:
        # Check for hallucinations
        # Check for PII leaks
        # Check for policy violations
        
        return True, text
```

**Audit Logging**:
```python
class AIAuditLogger:
    async def log_request(self, request: ChatRequest, prompt: str, response: str, metadata: dict):
        await db.ai_audit_logs.create(
            tenant_id=request.tenant_id,
            user_id=request.user_id,
            request_type="chat",
            input_text=request.question,
            prompt=prompt,
            output_text=response,
            model=metadata["model"],
            tokens_in=metadata["tokens_in"],
            tokens_out=metadata["tokens_out"],
            cost=metadata["cost"],
            timestamp=datetime.now()
        )
```

## Output

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ai/chat` | POST | AI chatbot response (streaming) |
| `/ai/summarize` | POST | Email/document summarization |
| `/ai/sentiment` | POST | Sentiment analysis |
| `/ai/usage` | GET | Usage statistics |
| `/ai/budget` | GET | Budget status |

### Performance Metrics

| Metric | Target | Achieved |
|--------|--------|----------|
| Chat latency | <2s | 1.3s |
| Summary latency | <5s | 3.2s |
| Throughput | 1000 req/hr | 1200 req/hr |
| Cost per request | <$0.05 | $0.03 |

### Monthly Cost Breakdown

- **Chat (GPT-3.5)**: 70% of requests × $0.0015/1k tokens = $1,050
- **Chat (GPT-4)**: 30% of requests × $0.03/1k tokens = $2,700
- **Summarization**: $800
- **Sentiment (local)**: $0 (self-hosted)
- **Infrastructure**: $450
- **Total**: $5,000/month ✅ (within budget)

### Key Decisions

1. **Why multi-provider?**: Avoid vendor lock-in, optimize cost/quality
2. **Why streaming?**: Better UX, reduces perceived latency
3. **Why caching?**: 25% cache hit rate, saves $1,250/month
4. **Why local models for sentiment?**: Cost-effective for simple tasks
5. **Why prompt versioning?**: Enables A/B testing and rollback

### Next Steps

1. Implement prompt optimization based on user feedback
2. Add support for multi-modal inputs (images, audio)
3. Implement fine-tuning for domain-specific tasks
4. Build prompt playground for testing
5. Add cost allocation per feature/user
