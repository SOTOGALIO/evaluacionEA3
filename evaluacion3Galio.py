'''Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
La empresa de eSports “eShirlitos”, necesita desarrollar un sistema que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. Para el funcionamiento del sistema se requiere las siguientes funcionalidades
1.
Registrar puntajes torneo
2.
Listar los todos puntajes
3.
Imprimir por Tipo
4.
Salir del programa
1.
Registrar puntajes torneo
Para registrar puntajes se requiere lo siguiente: Identificador de Jugador, Nombre y apellido del jugador, juego, puntaje obtenido. Por ejemplo, si el jugador compite en Fortnite y Fifa. Debe permitir seleccionar entre 1 de las 3 opciones e ingresar la cantidad de puntos obtenidos en esos dos juegos, también debe incluir su tipo (Principiante – Avanzado - Experto). Por lo tanto, un detalle de puntos del torneo podría verse registrado de la siguiente manera:
Id Jugador Nombre VALORANT FORNITE FIFA Tipo Mago Luis Jimenez 0 125000 3500 Principiante
Debe validar que todos los datos sean ingresados.
2.
Listar puntajes
Debe mostrar en la pantalla la lista de todos los puntajes registrados, similar al ejemplo anterior (opción 1).
3.
Imprimir por Tipo
Para imprimir por tipo, el usuario debe seleccionar alguno de los 3 tipos (Principiante – Avanzado - Experto). Estos tipos deben estar previamente definidos en algún tipo de colección de Python en el código.
Al seleccionar uno de los tipos, se generará un archivo de texto (.txt) con el detalle de los puntajes obtenidos por los jugadores del tipo seleccionado. Este debe tener la misma forma del registro completo de las opciones anteriores, pero en archivo de texto.
Cada opción de la aplicación debe desarrollarse en una función que debe llamarse desde el programa principal.
4.
Salir del programa
El programa debe funcionar hasta que el usuario decida salir.'''


print("Menu")
print("1.Registrar puntajes torneo")
print("2.Listar los todos puntajes")
print("3.Imprimir por Tipo")
print("4.Salir del programa")

def registrar_puntajes_torneo():

    jugadores = []

    print("Ingrese datos del jugador:")
    id = input("ingrese id del jugador: ")
    nombre = input("ingrese nombre del jugador: ")
    puntaje_valorant = int(input("ingrese puntaje valorant: "))
    puntaje_fornite = int(input("ingrese puntaje fornite: "))
    puntaje_fifa = int(input("ingrese puntaje fifa: "))
    tipo = input("Ingrese tipo: ")
    return 
    

def listar_puntajes():
    return 

def imprimir_por_tipo():
    return

while True:
    try:
        opcion= int(input("ingrese una opcion: "))
    

        if opcion == 1:
            print("Registrar puntajes")
            registrar_puntajes_torneo()
        elif opcion == 2:
            print("lista de puntajes")
        elif opcion == 3:
            print("imprimir por tipo")
        elif opcion == 4:
            print("Fin del programa")
            break

        elif opcion > 4 or opcion <= 0:
            print ("Ingrese una opcion valida")
    
    except:
            print("Ingrese una opcion valida")
