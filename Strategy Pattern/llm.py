from abc import ABC, abstractmethod
from typing import Dict

# Abstract Strategy Interface
class LLMStrategy(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response for the given prompt.
        Subclasses should implement the actual API call or mock logic.
        """
        pass

# Concrete Strategies

class OpenAIStrategy(LLMStrategy):
    def __init__(self, model: str = "gpt-4o", api_key: str = None):
        self.model = model
        self.api_key = api_key  # In real code, load from env or config

    def generate(self, prompt: str, **kwargs) -> str:
        # Placeholder for real OpenAI API call
        # In production, use openai Python client or httpx/requests
        temperature = kwargs.get("temperature", 0.7)
        return f"[OpenAI ({self.model})] Response to: '{prompt}' (temp={temperature})"

class AnthropicStrategy(LLMStrategy):
    def __init__(self, model: str = "claude-3-5-sonnet-20240620", api_key: str = None):
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str, **kwargs) -> str:
        max_tokens = kwargs.get("max_tokens", 1024)
        return f"[Anthropic ({self.model})] Response to: '{prompt}' (max_tokens={max_tokens})"

class GrokStrategy(LLMStrategy):
    def __init__(self, model: str = "grok-beta", api_key: str = None):
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str, **kwargs) -> str:
        temperature = kwargs.get("temperature", 0.8)
        return f"[Grok ({self.model})] Response to: '{prompt}' (temp={temperature})"

# Context that uses the selected strategy
class LLMClient:
    def __init__(self, strategy: LLMStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: LLMStrategy):
        """Dynamically switch provider at runtime"""
        self._strategy = strategy

    def generate(self, prompt: str, **kwargs) -> str:
        return self._strategy.generate(prompt, **kwargs)

# Optional: Factory to create strategies by name
class LLMFactory:
    _strategies: Dict[str, type] = {
        "openai": OpenAIStrategy,
        "anthropic": AnthropicStrategy,
        "grok": GrokStrategy,
    }

    @classmethod
    def create(cls, provider: str, **config) -> LLMStrategy:
        strategy_class = cls._strategies.get(provider.lower())
        if not strategy_class:
            raise ValueError(f"Unsupported provider: {provider}. Available: {list(cls._strategies.keys())}")
        return strategy_class(**config)

# Example usage
if __name__ == "__main__":
    # Create client with initial provider via factory
    client = LLMClient(LLMFactory.create("grok"))

    prompt = "Explain the strategy pattern in one sentence."

    # Use Grok
    print("Using Grok:")
    print(client.generate(prompt))
    print()

    # Switch to OpenAI
    client.set_strategy(LLMFactory.create("openai", model="gpt-4o"))
    print("Using OpenAI:")
    print(client.generate(prompt, temperature=0.5))
    print()

    # Switch to Anthropic
    client.set_strategy(LLMFactory.create("anthropic"))
    print("Using Anthropic:")
    print(client.generate(prompt, max_tokens=500))