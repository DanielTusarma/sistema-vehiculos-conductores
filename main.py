from models.Conductor import Conductor
from models.TipoVehiculos import Moto, Carro, Camion
from services.JornadaService import JornadaService

def main():
    # Crear conductores
    conductor_moto = Conductor("Juan Perez", "12345678", "A2")
    conductor_carro = Conductor("Ana Gomez", "87654321", "B1")
    conductor_camion = Conductor("Luis Torres", "11223344", "B2")
    conductor_carro2 = Conductor("Maria Lopez", "44332211", "B1") 

    # Crear vehículos
    moto1 = Moto("Yamaha", "YZF-R3", "321cc", casco=True)
    carro1 = Carro("Toyota", "Corolla", "1600cc", revision_tecnica=True)
    camion1 = Camion("Mercedes", "Actros", "10000cc", planilla=True, maximo_peso_toneladas=18)

    # Crear servicio
    servicio = JornadaService()

    # Probar iniciar jornada y mover vehículos
    print("=== MOTO ===")
    servicio.asignar_vehiculo(conductor_moto, moto1)
    servicio.iniciar_jornada_conductor(conductor_moto)
    moto1.mover()

    print("\n=== CARRO ===")
    servicio.asignar_vehiculo(conductor_carro, carro1)
    servicio.iniciar_jornada_conductor(conductor_carro)
    carro1.mover()

    print("\n=== CAMION ===")
    servicio.asignar_vehiculo(conductor_camion, camion1)
    servicio.iniciar_jornada_conductor(conductor_camion)
    camion1.mover()
    
    print("\n=== INFORMACION DE LOS CONDUCTORES ===")
    servicio.mostrar_info(conductor_moto)
    servicio.mostrar_info(conductor_carro)
    servicio.mostrar_info(conductor_camion)
    servicio.mostrar_info(conductor_carro2)
    
if __name__ == "__main__":
    main()
