from abc import ABC, abstractmethod

class BaseAgent(ABC):
    name = "base"

    def can_handle(self, query: str) -> bool:
        return True

    @abstractmethod
    def handle(self, query: str) -> str:
        raise NotImplementedError
