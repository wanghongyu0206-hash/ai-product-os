# AI Service Skill

## Goal

Design and implement AI-powered backend services that integrate LLM APIs, manage AI workflows, and deliver intelligent features to applications.

## When To Use

- Building AI chatbots and conversational interfaces
- Implementing content generation features
- Creating AI-powered recommendation systems
- Integrating multiple LLM providers
- Managing AI model costs and quotas
- Implementing prompt engineering pipelines
- Building AI agent workflows
- Adding semantic analysis features

## Workflow

### Step 1

Analyze AI service requirements.

Identify:
- AI capabilities needed (chat, generation, classification, etc.)
- LLM providers (OpenAI, Anthropic, local models)
- Throughput and latency requirements
- Cost constraints and budgets
- Compliance requirements (data privacy, content filtering)

### Step 2

Design AI service architecture.

Define:
- Service layer structure (API, orchestration, LLM clients)
- Request/response models
- Error handling and retry strategies
- Rate limiting and quota management
- Caching strategies
- Async processing for long-running tasks

### Step 3

Design LLM integration layer.

Implement:
- Provider abstraction (swap providers easily)
- Model selection logic (cost vs quality trade-offs)
- Prompt templates and management
- Token counting and cost estimation
- Streaming responses
- Fallback strategies

### Step 4

Design prompt engineering pipeline.

Create:
- System prompts for different use cases
- Context injection patterns
- Few-shot examples
- Prompt versioning and testing
- A/B testing framework
- Prompt optimization workflow

### Step 5

Design AI workflow orchestration.

Implement:
- Multi-step AI pipelines (e.g., classify → generate → validate)
- Agent frameworks for complex tasks
- Tool calling and function execution
- Conversation state management
- Memory and context windows

### Step 6

Design cost management and monitoring.

Plan:
- Token usage tracking per tenant/user
- Budget limits and alerts
- Cost optimization strategies (caching, smaller models)
- Usage analytics and reporting
- Rate limiting to prevent abuse

### Step 7

Design safety and compliance.

Implement:
- Content filtering (toxicity, PII detection)
- Input/output validation
- Audit logging for AI decisions
- Data privacy controls
- Bias detection and mitigation

### Step 8

Document AI service architecture.

Create:
- Service architecture diagram
- API specifications
- Prompt library documentation
- Configuration guide
- Monitoring and alerting setup

## Rules

1. Abstract LLM providers—don't hardcode to one vendor.
2. Always implement retry logic with exponential backoff.
3. Use streaming responses for better user experience.
4. Cache responses when possible to reduce costs.
5. Monitor token usage and costs per request.
6. Implement content filtering for safety.
7. Version and test prompts like code.
8. Use smaller models for simple tasks, save GPT-4 for complex ones.

## Output

- AI service architecture diagram
- LLM integration layer design
- Prompt engineering pipeline
- AI workflow orchestration design
- Cost management strategy
- Safety and compliance plan
- API specifications
- Monitoring and alerting configuration

## Quality Criteria

- LLM integration is provider-agnostic
- Error handling is robust (retries, fallbacks)
- Cost management is comprehensive
- Prompts are versioned and tested
- Content filtering is implemented
- Monitoring covers usage, latency, and errors
- API is well-documented and easy to use
- Compliance requirements are met
