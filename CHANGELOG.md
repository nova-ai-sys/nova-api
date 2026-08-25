# Changelog

## [0.10.1](https://github.com/nova-ai-sys/nova-api/compare/nova-api-v0.10.0...nova-api-v0.10.1) (2026-08-25)


### Features

* updated README.md ([485785d](https://github.com/nova-ai-sys/nova-api/commit/485785d777a2edba0d7e3d9272ee305d2033c192))

## [0.10.0](https://github.com/nova-ai-sys/nova-api/compare/nova-api-v0.9.0...nova-api-v0.10.0) (2026-08-25)


### ⚠ BREAKING CHANGES

* the API no longer accepts or requires an Authorization header, and the connections endpoints no longer report is_admin.

### Features

* **a2a:** A2A orchestrator — planner, executor, budgets and live run diagrams ([#15](https://github.com/nova-ai-sys/nova-api/issues/15)) ([a21eb1d](https://github.com/nova-ai-sys/nova-api/commit/a21eb1d6d3e84c307a30d5b5ebaecc79e7418b77))
* add MCP server, Streamlit UI, tool modules, and full documentation ([1b99687](https://github.com/nova-ai-sys/nova-api/commit/1b99687647b254e6d962300ae83a33543207309e))
* add multi-provider llm support with ollama openai and anthropic ([adde9ef](https://github.com/nova-ai-sys/nova-api/commit/adde9ef06e13eb00afe01bff5e47cca5cf949241))
* add roadmap deps, structlog logging, correlation ID middleware, memory models and DB init (Phase 1-2) ([9e12bd0](https://github.com/nova-ai-sys/nova-api/commit/9e12bd048b00892a06bac3b8248a52bd5a6ce512))
* add session listing and provider settings endpoints ([4acf52b](https://github.com/nova-ai-sys/nova-api/commit/4acf52b93f1faa970dc39449ca68ddb16fd2bed0))
* added landing page ([2abce0c](https://github.com/nova-ai-sys/nova-api/commit/2abce0c54189c355c59a0f028ce2aeede0d94aff))
* auth system (Cognito), user profiles, API keys, and GPU scaling ([4a38e12](https://github.com/nova-ai-sys/nova-api/commit/4a38e12f783959cd3bb618ee938068b822ed9e43))
* auto-inject knowledge base context into agent turns ([b275747](https://github.com/nova-ai-sys/nova-api/commit/b2757474841c1894ca14e02c6407dc8b6bd184a4))
* changed to new rebrand ([#17](https://github.com/nova-ai-sys/nova-api/issues/17)) ([16aa6d4](https://github.com/nova-ai-sys/nova-api/commit/16aa6d46f2de1106ebb005aa6ac4e236ec854b21))
* implemented history, folders, memory and tool for token count ([0444601](https://github.com/nova-ai-sys/nova-api/commit/04446013422af80c18bda6de9245d9492d4df5f8))
* **k8s:** add AWS EKS deployment with CI/CD pipeline ([79c205e](https://github.com/nova-ai-sys/nova-api/commit/79c205e5cfa48dae947185b14c88aa64cf6e8d2f))
* **mcp-connections:** added connections to Google, Microsoft and GitHub per user, improved provider selector and overall visibility of the application ([#13](https://github.com/nova-ai-sys/nova-api/issues/13)) ([c26f182](https://github.com/nova-ai-sys/nova-api/commit/c26f18210eefc3544a1ce01b5520ce41bcaa63eb))
* migrate from OpenAI API keys to local Ollama LLM models ([021ae50](https://github.com/nova-ai-sys/nova-api/commit/021ae502c016d20e4a7d06ce5545e04000ec89cf))
* react UI, streaming, MCP client, runtime settings ([4dcdd87](https://github.com/nova-ai-sys/nova-api/commit/4dcdd8710511c7ee1d66d033ffdd397814dbd6ce))
* split the agent backend into its own repository ([2b0449d](https://github.com/nova-ai-sys/nova-api/commit/2b0449db15296d99931889de8abb525bbd1ad521))
* update README.md, added versioning ([f561113](https://github.com/nova-ai-sys/nova-api/commit/f561113d60a844ab0b8b473bb0f69251dce29cd9))
* update tests and README ([b0b6d72](https://github.com/nova-ai-sys/nova-api/commit/b0b6d726d2c9cbb98683da6bd407a1274aa1cd6e))
* **US1:** conversational memory - fact extraction, episodic memory, memory context injection, API routes and UI ([0e64056](https://github.com/nova-ai-sys/nova-api/commit/0e6405640a169dd9c08663e6768a18f0a032b964))
* **US2:** RAG knowledge base - ChromaDB vector store, document ingestion, rag_search tool, API routes and UI ([04d7f25](https://github.com/nova-ai-sys/nova-api/commit/04d7f25b7b3d36febd1bc4c87077f0474914ff0c))
* **US3:** web search tool with Tavily primary and DuckDuckGo fallback ([ab2030d](https://github.com/nova-ai-sys/nova-api/commit/ab2030dc8ccf40aec9bcbf8f9abba921742f74f0))
* **US4:** sandboxed Python code execution tool + register web_search and execute_python in agent graph ([d6f05e0](https://github.com/nova-ai-sys/nova-api/commit/d6f05e06bf0b5713f08a2b42097ec46aff9eed3e))
* **US5:** professional landing page with docs, dynamic GitHub roadmap ([#6](https://github.com/nova-ai-sys/nova-api/issues/6)) ([36df3ff](https://github.com/nova-ai-sys/nova-api/commit/36df3fff939f51d01667a8625b49d29d73c652ee)), closes [#5](https://github.com/nova-ai-sys/nova-api/issues/5)
* **US5:** scheduled tasks - APScheduler manager, CRUD API, execution logs, enhanced health endpoint, and scheduler UI ([3599789](https://github.com/nova-ai-sys/nova-api/commit/3599789a3cd2ea601cee2309679d978298021086))


### Bug Fixes

* add error handling to API endpoints and migrate routes to structlog ([3300c5a](https://github.com/nova-ai-sys/nova-api/commit/3300c5a0e1bcb54f41b713edad0cdf625f1fdacf))
* **ci:** let release-please read its config file ([5ee18ca](https://github.com/nova-ai-sys/nova-api/commit/5ee18ca60af4d3a9209fef08a86382b30d0e5277))
* created snapshot for better view the roadmap on public landing page ([7eb91aa](https://github.com/nova-ai-sys/nova-api/commit/7eb91aacf6ff16dc4d4ffa16f7d28377af359903))
* **k8s:** use actual ECR images and add imagePullPolicy Always ([eeec83a](https://github.com/nova-ai-sys/nova-api/commit/eeec83a6ac77407cef28fd54ad4edd427fabc268))


### Refactoring

* remove unused user api keys ([e3030f3](https://github.com/nova-ai-sys/nova-api/commit/e3030f3c55c03e7b17114c4072db986c98b975c6))


### Documentation

* rewrite the readme and track the agent instructions ([cce6976](https://github.com/nova-ai-sys/nova-api/commit/cce697637faff4026f8746b2286c7afa30fd51be))


### Miscellaneous

* **main:** release 0.4.0 ([8eeb12b](https://github.com/nova-ai-sys/nova-api/commit/8eeb12b1b2f31035a779ade12a0fc274534d5ac5))
* **main:** release 0.5.0 ([#8](https://github.com/nova-ai-sys/nova-api/issues/8)) ([f20c94e](https://github.com/nova-ai-sys/nova-api/commit/f20c94ed029a176642899bff6f3f7095cee5de82))
* **main:** release 0.6.0 ([#12](https://github.com/nova-ai-sys/nova-api/issues/12)) ([6cfb744](https://github.com/nova-ai-sys/nova-api/commit/6cfb7446bb0419ba9813225fdbb103f4164fb974))
* **main:** release 0.7.0 ([e3e1d4a](https://github.com/nova-ai-sys/nova-api/commit/e3e1d4a104b12aab9d0ca93e82619de6747a8fc4))
* **main:** release 0.8.0 ([93c6cae](https://github.com/nova-ai-sys/nova-api/commit/93c6cae04d321b8d5f2c7962bdeb49470c1bea8d))
* **master:** release 0.2.0 ([#2](https://github.com/nova-ai-sys/nova-api/issues/2)) ([1f0b66c](https://github.com/nova-ai-sys/nova-api/commit/1f0b66c8a78e648a0f0351c5243bae39c85f22e7))
* **master:** release 0.3.0 ([#3](https://github.com/nova-ai-sys/nova-api/issues/3)) ([0c0f37e](https://github.com/nova-ai-sys/nova-api/commit/0c0f37eda0cb2c7bc17fd468a6252118e97ae7cd))
* remove all Kubernetes/EKS infrastructure and manifests ([990677b](https://github.com/nova-ai-sys/nova-api/commit/990677ba975bb9d5d64c63b57a96d2b986624664))
* stop tracking CLAUDE.md ([af98b60](https://github.com/nova-ai-sys/nova-api/commit/af98b60702a62b45d3692c99fbc37a89caa63131))
* switch GPU nodegroup to on-demand, update docs and costs ([8ce09c1](https://github.com/nova-ai-sys/nova-api/commit/8ce09c153c9babd84c92e95cf6dec6607f399f3e))
