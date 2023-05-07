class Registro:
    __temperatura = 0.0
    __humedad = 0.0
    __presionatm = 0.0

    def __init__(self, temperatura=0.0, humedad=0.0, presionatm=0.0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presionatm = presionatm

    def __str__(self) -> str:
        return f'[Temperatura: {self.__temperatura}, Humedad: {self.__humedad}, Presión Atmosférica: {self.__presionatm}]'

    def get_temperatura (self):
        return self.__temperatura
    def get_humedad(self):
        return self.__humedad
    def get_presion(self):
        return self.__presionatm
