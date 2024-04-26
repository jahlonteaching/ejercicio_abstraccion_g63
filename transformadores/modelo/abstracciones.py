from abc import ABC, abstractmethod

class Transformador(ABC):
    @abstractmethod
    def transformar(self, text: str, tipo: int) -> str:
        pass