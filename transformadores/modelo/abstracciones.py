from abc import ABC, abstractmethod

class Transformador(ABC):

    @abstractmethod
    def traformar(self, string: str, type: int) -> str:
        pass