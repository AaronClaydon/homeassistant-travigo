"""Custom types for travigo."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import TravigoApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type TravigoConfigEntry = ConfigEntry[TravigoData]


@dataclass
class TravigoData:
    """Data for the Blueprint integration."""

    client: TravigoApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
