from abc import ABC, abstractmethod
from .Motor import Motor

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: int, motor: Motor, tipo: str) -> None:
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo = tipo
    
    @abstractmethod
    def iniciar_jornada(self) -> None:
        pass
    
    @property
    def marca(self) -> str:
        return self._marca
    
    @property
    def modelo(self) -> int:
        return self._modelo
    
    @property
    def tipo(self) -> str:
        return self._tipo