#Ejercicio 3
import csv
from registrometeorologico import Registro
from clasemenu import Menu

if __name__ == '__main__':
    m = 31   #cantidad de dias del mes
    d = 24    #cantidad de horas del dia
    lista = []  # creo la matriz bidimensional
    for i in range(m):
        lista.append([None]*d)

    archivo = open('mes.csv', 'r')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        dia = int(fila[0])
        hora = int(fila[1])
        unainstancia = Registro(float(fila[2]), float(fila[3]), float(fila[4]))
        lista[dia-1][hora-1] = unainstancia
    print(archivo)
    archivo.close()

    print("Ingrese la Opcion")
    print("1: Mostrar para Cada Variable el dia y hora de menor y mayor \n")
    print("2: Indicar la temperatura promedio mensual por cada hora")
    print("3: Listar los valores de las tres variables \n")
    op = int(input('4:Salir\n'))
    menudeopciones = Menu(lista, op)
    menudeopciones.menu()
