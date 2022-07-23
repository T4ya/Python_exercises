#@T4ya (YESID ORTIZ)

#1. Dados dos números enteros, retornar el producto si este es menor o igual a 100, de lo contrario, retornar la suma


def ej1():

    #Inputs
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))

        except:
            print ("Error, ingrese números enteros")
        break

    if (num1 * num2) <= 100:
        print ("El producto de los dos números es: ", num1 * num2)
    else:
        print ("La suma de ambos números es: ", num1 + num2)
ej1()
