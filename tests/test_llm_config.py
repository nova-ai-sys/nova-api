"""Tests for ChatOllama configuration (T009).

Verifies that the LLM client is initialised with the expected keep_alive,
timeout, and num_ctx parameters read from environment variables.
"""

import os
from unittest.mock import patch

import httpx


def test_llm_default_keep_alive():
    """ChatOllama should be configured with keep_alive=-1 by default."""
    from agent.llm import KEEP_ALIVE
    assert KEEP_ALIVE == -1, f"Expected keep_alive=-1, got {KEEP_ALIVE}"


def test_llm_default_timeout():
    """ChatOllama should use a 120-second timeout by default."""
    from agent.llm import LLM_TIMEOUT
    assert LLM_TIMEOUT == 120.0, f"Expected timeout=120.0, got {LLM_TIMEOUT}"


def test_llm_num_ctx_defaults_above_ollama_minimum():
    """NOVA must ask for a context window large enough for its own prompt.

    Ollama defaults to 2048 tokens, which the system prompt plus the bound
    tool schemas exhaust on their own — the conversation history then gets
    silently dropped.

    The floor is what matters, not the exact figure: pinning an exact value
    made this test pass only on machines whose ``.env`` happened to set
    ``NOVA_NUM_CTX``, and fail on every clean checkout once the default was
    raised.
    """
    from agent.llm import NUM_CTX, _DEFAULT_NUM_CTX

    assert _DEFAULT_NUM_CTX >= 8192, (
        f"the built-in default dropped to {_DEFAULT_NUM_CTX}; NOVA's own prompt "
        "no longer fits"
    )

    override = os.getenv("NOVA_NUM_CTX")
    expected = int(override) if override else _DEFAULT_NUM_CTX
    assert NUM_CTX == expected, f"Expected NUM_CTX={expected}, got {NUM_CTX}"


def test_build_ollama_kwargs_has_keep_alive():
    """_build_ollama_kwargs must include keep_alive."""
    from agent.llm import _build_ollama_kwargs
    kwargs = _build_ollama_kwargs()
    assert "keep_alive" in kwargs
    assert kwargs["keep_alive"] == -1


def test_build_ollama_kwargs_has_timeout():
    """_build_ollama_kwargs must include httpx timeout in client_kwargs."""
    from agent.llm import _build_ollama_kwargs
    kwargs = _build_ollama_kwargs()
    assert "client_kwargs" in kwargs
    assert "timeout" in kwargs["client_kwargs"]
    assert isinstance(kwargs["client_kwargs"]["timeout"], httpx.Timeout)
    assert "async_client_kwargs" in kwargs
    assert "timeout" in kwargs["async_client_kwargs"]


def test_build_ollama_kwargs_always_sets_num_ctx():
    """num_ctx must always be sent, so Ollama never falls back to its own default."""
    from agent.llm import _build_ollama_kwargs, NUM_CTX
    kwargs = _build_ollama_kwargs()
    assert kwargs.get("num_ctx") == NUM_CTX
    assert kwargs["num_ctx"] >= 4096


def test_build_ollama_kwargs_includes_num_ctx_when_set():
    """_build_ollama_kwargs includes num_ctx when the module-level value is set."""
    import agent.llm as llm_module
    original = llm_module.NUM_CTX
    try:
        llm_module.NUM_CTX = 8192
        kwargs = llm_module._build_ollama_kwargs()
        assert kwargs.get("num_ctx") == 8192
    finally:
        llm_module.NUM_CTX = original
