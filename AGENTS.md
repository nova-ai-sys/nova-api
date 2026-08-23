# NOVA API - Agent Instructions

## Project Overview
NOVA (Neural Orchestration & Virtual Agent) is a Python AI agent powered by
LangChain/LangGraph with a local Ollama LLM backend and a FastAPI REST API.
This repository holds the agent and the API; the web UI, the documentation and
the public site live in `nova-frontend`, `nova-docs` and `nova-landing`.

It runs on the user's own machine. There is no deployment and no authentication.

## Key Directories
- `agent/` - Core agent: LangGraph state graph, nodes, state management, LLM client, orchestrator
- `api/` - FastAPI backend: routes, schemas, database
- `tools/` - LangChain tools (calculator, datetime, file ops, token counter)
- `nova_mcp/` - MCP server/client (Model Context Protocol)
- `nova_a2a/` - Multi-agent orchestration (agent-to-agent)
- `connections/` - OAuth connections to Google, Microsoft and GitHub
- `memory/` - Conversation and episodic memory, plus the RAG pipeline
- `scheduler/` - APScheduler automations
- `tests/` - Python pytest tests

## Common Commands
- `uv run pytest tests/ -v` - Run Python tests
- `uv run uvicorn api.main:create_app --factory --reload` - Run API server
- `make test` - Run tests via Makefile

## Testing
Every test mocks the model. No real Ollama, Anthropic or OpenAI calls belong in
the suite, in CI or locally.
