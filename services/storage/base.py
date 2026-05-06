from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class StorageBackend(ABC):
    """Abstract storage backend base class."""

    @abstractmethod
    def load_accounts(self) -> list[dict[str, Any]]:
        """Load all account data."""
        pass

    @abstractmethod
    def save_accounts(self, accounts: list[dict[str, Any]]) -> None:
        """Save all account data."""
        pass

    @abstractmethod
    def load_auth_keys(self) -> list[dict[str, Any]]:
        """Load all auth key data."""
        pass

    @abstractmethod
    def save_auth_keys(self, auth_keys: list[dict[str, Any]]) -> None:
        """Save all auth key data."""
        pass

    @abstractmethod
    def health_check(self) -> dict[str, Any]:
        """Run a health check and return backend status."""
        pass

    @abstractmethod
    def get_backend_info(self) -> dict[str, Any]:
        """Return storage backend information."""
        pass
