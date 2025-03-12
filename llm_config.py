import os

class LLMConfig:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
    GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY", "your_google_gemini_api_key_here")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "your_claude_api_key_here")
    OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "your_ollama_api_key_here")

    PROVIDERS = {
        "openai": OPENAI_API_KEY,
        "google_gemini": GOOGLE_GEMINI_API_KEY,
        "claude": CLAUDE_API_KEY,
    }

    @classmethod
    def get_provider_key(cls, provider_name: str) -> str:
        return cls.PROVIDERS.get(provider_name, "")

if __name__ == "__main__":
    print("LLM Configuration:")
    for provider, key in LLMConfig.PROVIDERS.items():
        print(f"{provider}: {key}")