#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Laureano Cejas"
__email__ = "laurecejas2510@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica
    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    
    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print ("numero1= {} es mayor a numero2= {}".format(numero_1, numero_2))
    else:
        print("numero2= {} es mayor a numero1= {}".format(numero_2, numero_1))

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if numero_1 > 0:
        print("numero ingresado es positivo")
    elif numero_1 < 0:
        print("numero ingresado es negativo")
    else: 
        print("numero ingresado es igual a 0")
    
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 > 0 and numero_1 < 100):
        print("se cumple la condicion AND")
    else:
        print("no se cumple la condicion AND")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10 or numero_2 > -2):
        print("se cumple la condicion del operador OR")
    else:
        print("no se cumple la condicion del operador OR")

def ej2():
    # Ejemplos variables de texto
    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("{} es mayor que {}".format(texto_1, texto_2))
    else:
        print("{} es mayor que {}".format(texto_2, texto_1)) 

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    palabra_1 = len (texto_1)
    palabra_2 = len (texto_2)

    if palabra_1 > palabra_2:
        print("{} tiene mayor cantidad de caracter que {}".format(texto_1, texto_2))
    else: 
        print("{} tiene mayor cantidad de caracter que {}".format(texto_2, texto_1))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    caracter_inicial1 = texto_1 [0]
    caracter_inicial2 = texto_2 [0]

    if caracter_inicial1 > caracter_inicial2:
        print("{} tiene la primer letra mayor que {}".format(texto_1, texto_2))
    else:
        print("{} tiene la primer letra mayor que {}".format(texto_2, texto_1))
        
    # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    copia_texto_1 = texto_1

    if texto_1 == copia_texto_1:
        print("texto_1 es igual a la copia_texto 1")
    if texto_2 != copia_texto_1:
        print("texto_2 es distinto a la copia_texto1")

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 3
    numero_2 = 4

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print ("Resp=1")
        else:
            print ("Resp=2")
    elif numero_2 > 5: 
        print("Resp=3")
    else:
        print("Resp=4")
        
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 90:
        print ("A")
    else:
        if puntaje >= 80:
            print ("B")
        else:
            if puntaje >= 70:
                print ("C")
            else:
                if puntaje >= 60:
                    print("D")
                else:
                    if puntaje < 60:
                        print("F")


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("{} es mayor que {}".format(texto_1, texto_2))
    else:
        print("{} es mayor que {}".format(texto_2, texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    
    numero_1 = 5
    numero_2= 7

    if numero_1 > numero_2:
        print ("{} es mas grande que {}".format(numero_1, numero_2))
    else:
        print(" {} es mas grande que {}".format(numero_2, numero_1))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

    # Respuesta: se debe a la tabla del código ASCII nació para reordenar 
    # y expandir el conjunto de símbolos y caracteres

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
