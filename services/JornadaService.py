from models.Conductor import Conductor
from models.Vehiculo import Vehiculo
from models.VehiculosDisponibles import VehiculosDisponibles

tipos_licencias = {
    "A2": [VehiculosDisponibles.MOTO],
    "B1": [VehiculosDisponibles.CARRO],
    "B2": [VehiculosDisponibles.CARRO, VehiculosDisponibles.CAMION]
    }

class JornadaService:
    
    def __init__(self):
        self.asignaciones = {}
        
    def asignar_vehiculo(self, conductor: Conductor, vehiculo: Vehiculo) -> None:
        self.asignaciones[conductor] = vehiculo
        
    def iniciar_jornada_conductor(self, conductor: Conductor) -> None:
        vehiculo = self.asignaciones.get(conductor)
        
        if not vehiculo:
            raise ValueError(f"El conductor {conductor.nombre} no tiene un vehículo asignado")
        
        tipo_vehiculo = vehiculo.tipo
        licencias_permitidas = tipos_licencias.get(conductor.licencia, [])
        if tipo_vehiculo in licencias_permitidas:
            vehiculo.iniciar_jornada()
        else:
            raise PermissionError(f"El conductor con licencia {conductor.licencia} no está autorizado para conducir un {tipo_vehiculo}")
        
    def mostrar_info(self, conductor: Conductor) -> None:
        vehiculo = self.asignaciones.get(conductor)
        if vehiculo:
            print(f"Conductor: {conductor.nombre} - Vehículo: {vehiculo.tipo} Marca: {vehiculo.marca} Modelo: {vehiculo.modelo}")
        else:
            print(f"Conductor: {conductor.nombre} no tiene un vehículo asignado.")
