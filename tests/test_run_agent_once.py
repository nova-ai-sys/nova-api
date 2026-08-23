"""Tests for the single-agent turn helper.

``run_agent_once`` is no longer the CLI's entry point — the CLI is gone — but
it is still what the scheduler runs for an automation, and what the
orchestrator falls back to when the planner declines a request. These tests
cover the contract those two callers depend on: the fresh state it builds, the
history it carries forward, and the fact that it does not mutate the state it
was handed.

The compiled graph is stubbed, so no LLM and no Ollama are involved.
"""

from __future__ import annotations

from typing import Any, Dict

import pytest
from langchain_core.messages import AIMessage, HumanMessage

from agent import graph as graph_mod


class _StubGraph:
    """Stands in for the compiled LangGraph runnable.

    Records the state it was invoked with, and answers with that state plus an
    assistant reply and some token accounting — the shape a real turn returns.
    """

    def __init__(self, reply: str = "42", tokens: int = 7):
        self.reply = reply
        self.tokens = tokens
        self.seen: Dict[str, Any] | None = None

    async def ainvoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.seen = state
        return {
            **state,
            "messages": list(state["messages"]) + [AIMessage(content=self.reply)],
            "total_tokens": state.get("total_tokens", 0) + self.tokens,
            "iteration_count": state.get("iteration_count", 0) + 1,
        }


@pytest.fixture
def stub_graph(monkeypatch):
    """Replace the compiled graph for the duration of one test."""
    stub = _StubGraph()
    monkeypatch.setattr(graph_mod, "get_compiled_graph", lambda: stub)
    return stub


@pytest.mark.asyncio
async def test_a_new_turn_starts_from_an_empty_state(stub_graph):
    """With no prior state the helper builds one rather than failing."""
    result = await graph_mod.run_agent_once("what is 6 times 7?")

    assert stub_graph.seen is not None
    assert stub_graph.seen["memory_context"] == ""
    assert stub_graph.seen["tool_results"] == []
    assert stub_graph.seen["iteration_count"] == 0
    assert stub_graph.seen["total_tokens"] == 0

    # The user's message reaches the graph, and the reply comes back last.
    assert isinstance(stub_graph.seen["messages"][0], HumanMessage)
    assert stub_graph.seen["messages"][0].content == "what is 6 times 7?"
    assert result["messages"][-1].content == "42"


@pytest.mark.asyncio
async def test_prior_messages_are_carried_into_the_turn(stub_graph):
    """A scheduled follow-up must see the conversation it belongs to."""
    prior = {
        "messages": [HumanMessage(content="remember 41"), AIMessage(content="noted")],
        "memory_context": "the number is 41",
        "tool_results": [{"tool": "calculator"}],
        "iteration_count": 3,
        "total_tokens": 120,
        "token_usage": None,
    }

    result = await graph_mod.run_agent_once("add one", state=prior)

    sent = stub_graph.seen["messages"]
    assert [m.content for m in sent] == ["remember 41", "noted", "add one"]
    assert stub_graph.seen["memory_context"] == "the number is 41"
    assert stub_graph.seen["tool_results"] == [{"tool": "calculator"}]

    # Token accounting accumulates instead of restarting — the scheduler
    # reports cost per task, and a reset would under-report every follow-up.
    assert result["total_tokens"] == 127
    assert result["iteration_count"] == 4


@pytest.mark.asyncio
async def test_the_caller_s_state_is_left_untouched(stub_graph):
    """The helper copies before appending.

    The orchestrator hands it the live session state and keeps using that dict
    afterwards; appending in place would duplicate the user's message.
    """
    messages = [HumanMessage(content="first")]
    prior = {
        "messages": messages,
        "memory_context": "",
        "tool_results": [],
        "iteration_count": 0,
        "total_tokens": 0,
        "token_usage": None,
    }

    await graph_mod.run_agent_once("second", state=prior)

    assert len(messages) == 1
    assert prior["messages"] is messages
    assert prior["total_tokens"] == 0
