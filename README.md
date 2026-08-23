<div align="center">

<img src=".github/nova-logo.png" alt="NOVA logo" width="160" />

# NOVA API

The agent core and REST API of **Neural Orchestration & Virtual Agent**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/thisisrobyn)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/thisisrobyn)
[![Stars](https://img.shields.io/github/stars/nova-ai-sys/nova-api?style=for-the-badge&color=f59e0b)](https://github.com/nova-ai-sys/nova-api/stargazers)

</div>

## What this is

The brain of NOVA: the agent loop, the multi-agent orchestrator, the tools,
memory and RAG, the scheduler, and the API the web UI talks to.

It runs **on your own machine, against your own Ollama**. There is no hosted
NOVA and no account to create.

## Install

You need [Ollama](https://ollama.com) and [uv](https://docs.astral.sh/uv/).

```bash
# 1. Models
ollama pull gemma3:4b          # chat
ollama pull nomic-embed-text   # embeddings for RAG

# 2. Configuration
cp .env.example .env

# 3. Dependencies
make install

# 4. Start it on port 8000
make api
```

Now start [nova-frontend](https://github.com/nova-ai-sys/nova-frontend) and
open it in your browser. This API has no interface of its own.

## Commands

| Command | What it does |
|---------|-------------|
| `make install` | Install dependencies |
| `make api` | Start the API on port 8000 |
| `make test` | Run the tests |
| `make mcp` | Start NOVA's MCP server |
| `make mcp-google` | Start the Gmail / Calendar / Drive server |
| `make mcp-microsoft` | Start the Outlook / Calendar / OneDrive server |
| `make mcp-github` | Start the GitHub server |

On Windows, `.\dev.ps1` starts the API in a new terminal.

## Layout

| Folder | What lives there |
|--------|-----------------|
| `agent/` | The agent loop, the orchestrator, state and LLM config |
| `api/` | FastAPI app, routes, schemas, middleware |
| `tools/` | The tools the agent can call |
| `memory/` | Conversation memory, episodes and the RAG pipeline |
| `scheduler/` | Scheduled automations |
| `nova_mcp/` | MCP client and servers |
| `nova_a2a/` | Multi-agent orchestration |
| `connections/` | OAuth for Google, Microsoft and GitHub |

## No login

NOVA is single-user by design. It listens on your machine, so there are no
accounts and no tokens. Credentials for connected services are encrypted at
rest under a single local identity.

If you expose this API beyond your own machine, put your own authentication in
front of it — it has none.

## The rest of NOVA

| Repository | What it is |
|------------|------------|
| [nova-frontend](https://github.com/nova-ai-sys/nova-frontend) | The web UI |
| [nova-docs](https://github.com/nova-ai-sys/nova-docs) | The documentation |
| [nova-landing](https://github.com/nova-ai-sys/nova-landing) | The public site |

Full documentation at **[nova.robyn.es/docs](https://nova.robyn.es/docs)**.

## License

MIT

---

<div align="center">
  Made with ❤️ by <a href="https://robyn.es">ROBYN</a>
</div>
