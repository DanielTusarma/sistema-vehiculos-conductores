from .Vehiculo import Vehiculo
from .Movible import Movible
from .VehiculosDisponibles import VehiculosDisponibles
    
class Moto(Vehiculo, Movible):
    def __init__(self, marca, modelo, motor, casco):
        super().__init__(marca, modelo, motor, VehiculosDisponibles.MOTO)
        self._casco = casco
    
    def iniciar_jornada(self) -> None:
        if self._casco:
            print(f"La moto de marca {self._marca}, modelo {self._modelo}")
            print("y con casco, listo para iniciar jornada.")
        else:
            raise ValueError("No se puede iniciar jornada sin casco")
        
    def mover(self) -> None:
        print("La moto se desplaza agilmente por la ciudad")
    
    
class Carro(Vehiculo, Movible):
    def __init__(self, marca, modelo, motor, revision_tecnica):
        super().__init__(marca, modelo, motor, VehiculosDisponibles.CARRO)
        self._revision_tecnica = revision_tecnica
        
    def iniciar_jornada(self) -> None:
        if self._revision_tecnica:
            print(f"El carro de marca {self._marca}, modelo {self._modelo}")
            print("y con revisión tecno-mecanica al dia, listo para iniciar jornada.")
        else:
            raise ValueError("El carro no puede iniciar jornada laboral sin tecno_mecanica al dia")
            
    def mover(self) -> None:
        print("El carro se mueve hacia las afueras de la ciudad")
            
class Camion(Vehiculo, Movible):
    def __init__(self, marca, modelo, motor, planilla, maximo_peso_toneladas):
        super().__init__(marca, modelo, motor, VehiculosDisponibles.CAMION)
        self._planilla = planilla
        self._maximo_peso_toneladas = maximo_peso_toneladas
        
    def iniciar_jornada(self) -> None:
        # Maximo peso no puede exceder las 20 toneladas
        if self._maximo_peso_toneladas <= 20 and self._planilla:
            print(f"El camión de marca {self._marca}, modelo {self._modelo}")
            print(f"con planilla de cargue y peso de {self._maximo_peso_toneladas} toneladas")
            print("listo para iniciar jornada.")
        else:
            raise ValueError("El camión no cumple con los requerimientos minimos para iniciar jornada")    
        
    def mover(self):
        print("El camión se mueve con mucha mercancia para otra ciudad")
    
    
