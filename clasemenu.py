from registrometeorologico import Registro
class Menu:
    __opcion = None
    __lista = None

    def __init__(self, lista, op):
        self.__lista = list
        self.__opcion = op

    def menorvalor(self, var):
        if var == "Humedad":
            min = -12121212
            for i in range(31):
                for j in range(24):
                    if self.__lista[i][j].get_humedad() < min:
                        min = self.lista[i][j].get_humedad()
                        dia = i + 1
                        hora = j + 1
            return dia, hora
        elif var == "Temperatura":
            min = -12121212
            for i in range(31):
                for j in range(24):
                    if self.__lista[i][j].get_temperatura() < min:
                        min = self.__lista[i][j].get_temperatura()
                        dia = i + 1
                        hora = j + 1
            return dia, hora
        elif var == "Presion":
            min = -122912912
            for i in range(31):
                for j in range(24):
                    if self.__lista[i][j].get_presion() < min:
                        self.__lista[i][j].get_presion()
                        dia = i + 1
                        hora = j + 1
        else:
            print("Hay Un Error para calcular el Minimo")

    def MostrarNumero(self):
        variables = ["Humedad", "Temperatura", "Presion"]
        for variable in len(variables):
            print("Para la Variable {} el dia y hora de menor valor es".format(variable, self.menorvalor(variables), self.mayorvalor(variables)))

    def Promedio(self):
        for i in range(30):
            x = 0
            for j in range(24):
                x += self.__lista[i][j].get_temperatura()
                print("El promedio del dia {} por cada hora es: {}".format(i + 1, x / 30))

    def Listado(self):
        dia = int(input("Ingrese un Numero de Dia para indicar las variables"))
        print("Hora          Temperatura        Humedad          Presion")
        for i in range(24):
            print("{}        {}        {}        {}".format(i + 1, self.__lista[dia][i].get_temperatura(), self.__lista[dia][i].get_humedad(), self.__lista[dia][i].get__humedad()))

    def menu(self):
        if self.__opcion == 1:
            self.MostrarNumero()
        elif self.__opcion == 2:
            self.Promedio()
        elif self.__opcion == 3:
            self.Listado()
        else:
            print("Error al Ingresar el Codigo")

