"""Identity the agent acts for when it reaches an external service.

NOVA runs on the user's own machine against their own Ollama, so there is
exactly one identity: the local operator. OAuth tokens are still stored under
a user id because the schema in :mod:`connections.store` is keyed by it, and
this module is the single place that answers "which one".

It stays a function rather than an inlined constant so the service tools and
the standalone MCP servers keep asking one place, and so restoring per-user
isolation later means changing this module alone.
"""

from __future__ import annotations

from connections.store import LOCAL_USER_ID


def get_current_user() -> str:
    """The user id every service tool should act as."""
    return LOCAL_USER_ID
