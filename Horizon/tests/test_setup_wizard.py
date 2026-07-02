from __future__ import annotations

from src.models import AIConfig, AIProvider
from src.setup import wizard


def test_configure_ai_allows_ollama_without_api_key(monkeypatch):
    answers = iter(
        [
            "ollama",
            "llama3.2",
            "http://nas.local:11434",
            "",
            "zh,en",
        ]
    )

    monkeypatch.setattr(wizard.Prompt, "ask", lambda *args, **kwargs: next(answers))
    monkeypatch.setattr(wizard.console, "print", lambda *args, **kwargs: None)

    config = wizard.configure_ai()

    assert config == AIConfig(
        provider=AIProvider.OLLAMA,
        model="llama3.2",
        base_url="http://nas.local:11434",
        api_key_env="",
        temperature=0.3,
        max_tokens=8192,
        languages=["zh", "en"],
    )


def test_ai_recommendations_available_for_ollama_without_api_key():
    config = AIConfig(
        provider=AIProvider.OLLAMA,
        model="llama3.1",
        api_key_env="",
    )

    assert wizard._ai_recommendations_available(config) is True


def test_ai_recommendations_require_api_key_for_cloud_provider(monkeypatch):
    config = AIConfig(
        provider=AIProvider.OPENAI,
        model="gpt-4",
        api_key_env="OPENAI_API_KEY",
    )
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    assert wizard._ai_recommendations_available(config) is False

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    assert wizard._ai_recommendations_available(config) is True
