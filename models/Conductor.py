class Conductor:
    def __init__(self, nombre: str, documento: str, licencia: str) -> None:
        self._nombre = nombre
        self._documento = documento
        self._licencia = licencia
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre no debe estar vacío")
        
    @property
    def documento(self) -> str:
        return self._documento
    
    @documento.setter
    def documento(self, documento: str) -> None:
        if isinstance(documento, str) and documento.strip():
            self._documento = documento
        else:
            raise ValueError("El documento no debe estar vacío")
    
    @property
    def licencia(self) -> str:
        return self._licencia
    
    @licencia.setter
    def licencia(self, licencia: str) -> None:
        if isinstance(licencia, str) and licencia.strip():
            self._licencia = licencia    
        else:
            raise ValueError("La licencia no debe estar vacía")
        
    