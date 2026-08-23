.PHONY: install api mcp mcp-google mcp-microsoft mcp-github clean help test

# Cross-platform: use `uv run` instead of hard-coded venv paths

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync
	@echo ""
	@echo "✅ Dependencies installed. Run 'make api' to start the backend."

api: ## Run the FastAPI backend (port 8000)
	@uv run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000 --reload-exclude .venv

mcp: ## Run the MCP server (stdio)
	@uv run python -m nova_mcp.server

mcp-http: ## Run the MCP server (HTTP/SSE)
	@MCP_TRANSPORT=http uv run python -m nova_mcp.server

mcp-google: ## Run the Google MCP server (stdio)
	@uv run python -m nova_mcp.servers.google

mcp-microsoft: ## Run the Microsoft MCP server (stdio)
	@uv run python -m nova_mcp.servers.microsoft

mcp-github: ## Run the GitHub MCP server (stdio)
	@uv run python -m nova_mcp.servers.github

test: ## Run tests
	@uv run pytest tests/ -v

clean: ## Remove build artifacts and cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache build dist *.egg-info
