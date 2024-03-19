"""Support for the TikTok TTS service."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.components.tts import (
    PLATFORM_SCHEMA,
    Provider,
    TextToSpeechEntity,
    TtsAudioType,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.components.tts import CONF_LANG
from .tiktokvoice import tts

from .const import (
    DEFAULT_LANG,
    SUPPORT_LANGUAGES,
)

_LOGGER = logging.getLogger(__name__)

SUPPORT_OPTIONS = [CONF_LANG]

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
    }
)


async def async_get_engine(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> TikTokProvider:
    """Set up TikTok speech component."""
    return TikTokProvider(hass, config[CONF_LANG])


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up TikTok speech platform via config entry."""
    DEFAULT_LANG = config_entry.data[CONF_LANG]
    async_add_entities([TikTokTTSEntity(config_entry, DEFAULT_LANG)])


class TikTokTTSEntity(TextToSpeechEntity):
    """The TikTok speech API entity."""

    def __init__(self, config_entry: ConfigEntry, voice: str) -> None:
        """Init TikTok TTS service."""
        self._voice = voice
        self._attr_name = f"TikTok {self._voice}"
        self._attr_unique_id = config_entry.entry_id

    @property
    def default_language(self):
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self):
        """Return a list of supported options."""
        return SUPPORT_OPTIONS

    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTS from TikTok."""
        data = tts(text=message, voice=language)

        if data[1] != "":
            _LOGGER.debug(
                "Error during processing of TTS request: %s", data[1], exc_info=False
            )
            raise HomeAssistantError(Exception("Error"))

        return "mp3", data[0]


class TikTokProvider(Provider):
    """The TikTok speech API provider."""

    def __init__(self, hass, lang):
        """Load TTS from TikTok."""
        self.hass = hass
        self._lang = lang
        self.name = "TikTok"

    @property
    def default_language(self):
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self):
        """Return a list of supported options."""
        return SUPPORT_OPTIONS

    def get_tts_audio(self, message, language, options):
        """Load TTS from google."""
        data = tts(text=message, voice=language)

        if data[1] != "":
            _LOGGER.exception("Error during processing of TTS request: %s", data[1])
            return None, None

        return "mp3", data[0]
