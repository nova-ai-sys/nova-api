# NOVA API

> Neural Orchestration & Virtual Agent — the agent core and its REST API.

The brain of NOVA: the LangGraph agent loop, the multi-agent orchestrator, the
tools, memory and RAG, the scheduler, and the FastAPI server the web UI talks
to. It runs **on your own machine, against your own Ollama** — there is no
hosted NOVA, and no account to create.

| Repository | What it is |
|------------|------------|
| **nova-api** (this one) | The agent and the REST API |
| [nova-frontend](https://github.com/nova-ai-sys/nova-frontend) | The web UI, the only interface |
| [nova-docs](https://github.com/nova-ai-sys/nova-docs) | The documentation, in Markdown |
| [nova-landing](https://github.com/nova-ai-sys/nova-landing) | The public site, nova.robyn.es |

## Quick start

```bash
# 1. Ollama, with the models NOVA uses
ollama pull gemma3:4b          # chat model
ollama pull nomic-embed-text   # embeddings for RAG

# 2. Configuration
cp .env.example .env           # then edit it

# 3. Dependencies (uv manages the environment)
make install

# 4. Start the API on port 8000
make api
```

Then start [nova-frontend](https://github.com/nova-ai-sys/nova-frontend) and
open it in your browser. The API on its own has no interface.

## Commands

| Command | What it does |
|---------|-------------|
| `make install` | Install dependencies with uv |
| `make api` | Start the FastAPI backend (port 8000) |
| `make test` | Run the test suite |
| `make mcp` | Start NOVA's own MCP server (stdio) |
| `make mcp-google` | Start the Google (Gmail/Calendar/Drive) MCP server |
| `make mcp-microsoft` | Start the Microsoft (Outlook/Calendar/OneDrive) MCP server |
| `make mcp-github` | Start the GitHub MCP server |

On Windows, `.\dev.ps1` starts the API in a new terminal.

## Layout

```
nova-api/
├── agent/          # LangGraph agent loop, orchestrator, nodes, state, LLM config
├── api/            # FastAPI app, routes, schemas, middleware, system metrics
├── tools/          # The tools the agent can call
├── memory/         # Conversation and episodic memory, plus the RAG pipeline
├── scheduler/      # APScheduler automations
├── nova_mcp/       # MCP client and servers (agent ↔ tool)
├── nova_a2a/       # Multi-agent orchestration (agent ↔ agent)
├── connections/    # OAuth connections to Google, Microsoft and GitHub
└── tests/          # pytest — every test mocks the model
```

## No authentication

NOVA is single-user by design. It runs on your machine, the API listens on
localhost, and there are no accounts, no tokens and no login. OAuth
credentials for connected services are encrypted at rest under a single local
identity (`connections/context.py`).

If you expose this API beyond your own machine, put your own authentication in
front of it — it has none of its own.

## Documentation

Everything lives in [nova-docs](https://github.com/nova-ai-sys/nova-docs), and
is published at [nova.robyn.es/docs](https://nova.robyn.es/docs).

## License

See the repository for licensing details.
