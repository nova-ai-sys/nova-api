# NOVA API — Claude Code Instructions
> Neural Orchestration & Virtual Agent

The agent core and REST API of NOVA, built on LangChain/LangGraph with a local
**Ollama** backend. It is a master's thesis (TFM) project.

NOVA is split across four repositories. This one holds all the Python: the
agent, the API, the tools, memory, the scheduler and the integrations. The web
UI is in `nova-frontend`, the documentation in `nova-docs`, the public site in
`nova-landing`.

It runs **only on the user's own machine.** There is no deployment, no hosting
and no authentication — see "No authentication" below before adding either.

---

## Repository Layout (real)

```
nova-api/
├── agent/            # Core: LangGraph graph, nodes, state, LLM client, logging
│   ├── graph.py      # Single-agent ReAct loop + the tool registry
│   ├── orchestrator.py # Supervisor graph over the nova_a2a workers
│   ├── nodes.py      # Graph nodes (reasoning, tools, memory)
│   ├── state.py      # Shared agent state (TypedDict)
│   ├── llm.py        # LLM factory / config
│   └── llm_client.py # LLM client wrapper
├── api/              # FastAPI backend
│   ├── main.py       # App factory (create_app)
│   ├── routes.py     # REST endpoints
│   ├── routes_connections.py # OAuth connection endpoints
│   ├── schemas.py    # Pydantic v2 models
│   ├── db.py         # Database access
│   ├── system_metrics.py # Host CPU / RAM / GPU counters (psutil + nvidia-smi)
│   └── middleware.py
├── tools/            # LangChain tools (@tool)
│   ├── calculator.py
│   ├── code_executor.py     # Sandboxed code execution
│   ├── datetime_tool.py
│   ├── files.py             # pandas / openpyxl file ops
│   ├── rag_tool.py          # Retrieval over Chroma
│   ├── web_search.py        # Tavily / DuckDuckGo
│   └── token_counter.py, token_visualizer.py, conversation_tokens.py
├── connections/      # OAuth connections to Google / Microsoft / GitHub
│   ├── providers.py   # Provider registry (endpoints, scopes, env vars)
│   ├── credentials.py # App client id/secret (database, env fallback)
│   ├── oauth.py       # Authorization URL, code exchange, token refresh
│   ├── github_app.py  # One-click GitHub App registration via manifest
│   ├── store.py       # Encrypted SQLite persistence + auto-refresh
│   ├── context.py     # The single local identity tools act as
│   ├── prompt.py      # Connection state injected into the system prompt
│   └── crypto.py      # Fernet encryption for secrets at rest
├── memory/           # Conversation, episodic, models, database + rag/
├── scheduler/        # APScheduler jobs: manager, store, models
├── nova_mcp/         # MCP (agent ↔ tool): server.py + client.py (fastmcp)
│   ├── servers/      # Per-account MCP servers: google.py, microsoft.py, github.py
│   └── builtin.py    # Binds those same tools into the agent graph in-process
├── nova_a2a/         # A2A (agent ↔ agent): multi-agent orchestration
│   ├── models.py     # Protocol types: AgentCard, Task, Artifact, TaskState
│   ├── card.py       # NOVA's public Agent Card (/.well-known/agent-card.json)
│   ├── registry.py   # Agent discovery: internal specs + remote peers (cards)
│   ├── agents/       # One module per worker: calendar, mail, research, docs, github, advisor
│   ├── worker.py     # In-process task execution (the builtin.py analog)
│   ├── client.py     # Outbound A2A: message/send to a remote agent
│   ├── budget.py     # Per-task execution budget + retry policy
│   ├── planner.py    # Request → task DAG, and repair plans on failure
│   ├── executor.py   # Runs the DAG in dependency waves, retries, cancels
│   ├── aggregator.py # Artifacts → the user's single answer
│   └── _tokens.py    # Token-usage extraction across provider shapes
├── tests/            # pytest
├── pyproject.toml    # uv-managed project
└── .env / .env.example
```

Keep this map in sync when directories change.

---

## Tech Stack (from `pyproject.toml`)

- **Python**: `>=3.10`, managed with **uv** (`uv.lock` is committed)
- **LLM**: local **Ollama** via `langchain-ollama` (not cloud by default)
- **Orchestration**: `langgraph` (1.x) + `langchain` (1.x)
- **MCP**: `langchain-mcp-adapters`, `fastmcp`, `mcp`
- **API**: `fastapi[standard]` + `uvicorn`
- **RAG**: `chromadb` + `langchain-chroma`, `pymupdf` for PDFs
- **Web search**: `tavily-python`, `duckduckgo-search`
- **Memory/scheduling**: `aiosqlite`, `sqlalchemy`, `apscheduler` (3.x)
- **Data**: `pandas`, `openpyxl`; **tokens**: `tiktoken`
- **Observability**: `structlog`

---

## Common Commands

Run Python via **uv** (never call `python`/`pip` directly):

- `uv run pytest tests/ -v` — run tests
- `uv run uvicorn api.main:create_app --factory --reload` — run the API server
- `make test` — tests via Makefile

On Windows the shell is PowerShell; `dev.ps1` is a helper script.

---

## Code Conventions

- Python 3.10+, type hints on all functions, Google-style docstrings
- Config via `pydantic` settings; read secrets with `os.getenv()` / `python-dotenv`
- **Never hardcode credentials.** Add any new env var to `.env.example`
- Log with `structlog` / `logging.getLogger(__name__)` — never `print()`
- Explicit error handling with specific exceptions

LangGraph:
- Agent state is a `TypedDict` in `agent/state.py`
- Nodes are async functions that return **partial** state dicts (never mutate global state)
- Use `add_messages` to accumulate messages

Tools:
- Define with the LangChain `@tool` decorator, clear docstrings, internal error handling
  (do not raise into the agent)
- For code-execution tools, enforce timeouts and restrict dangerous imports

API:
- All endpoints async, Pydantic v2 schemas, versioned paths
- The chat endpoints run the **orchestrator** (`agent/orchestrator.py`). The
  single-agent loop in `agent/graph.py` is not dead code: the orchestrator
  falls back to it when the planner declines to split a request, and the
  scheduler runs it directly.

Testing:
- `pytest` + `pytest-asyncio`; **mock the LLM** — no real Ollama, Anthropic or
  OpenAI calls, in CI or locally. A test that needs a live model is a test that
  needs rewriting; the suite used to be full of those and they all failed.

---

## No authentication

There is none, deliberately. NOVA is single-user and local: no accounts, no
JWT, no login. OAuth tokens for connected services are stored under one local
identity, resolved in `connections/context.py`.

Do not reintroduce an auth layer without being asked. If multi-user support
ever comes back, `connections/context.py` is the seam — everything downstream
already asks it who the acting user is.

---

## Working Agreements (for Claude Code)

- Ground every change in the real files above — verify a module/symbol exists
  before referencing it; the directory tree here reflects the current repo.
- Commits follow **Conventional Commits**; release-please handles versions and
  `CHANGELOG.md`, so never edit either by hand. `uv.lock` is managed too.
- **Write short commit messages.** One line saying what changed. Add a body
  only when the reason is not obvious, and keep it to a sentence or two.
- **No `Co-Authored-By` trailers** and no tool attribution in commit messages.
- **Never push unless asked.** Committing finished work is fine; pushing is a
  separate decision that belongs to the user.
- Keep changes modular within `agent/ tools/ memory/ scheduler/ api/ nova_mcp/
  nova_a2a/ connections/`.
- Changes that alter the REST contract need the matching change in
  `nova-frontend` and a docs update in `nova-docs`.
