# Escribir una función que lea dos ficheros csv con una
# lista larga de datos de personas (50 personas y 1000 personas)
import csv

def lectorDoc(archivo):
    with open (archivo , 'r') as file :    #función 1
    
        for i in (file.readlines()):
            i.split()
            print(i)
            

lectorDoc('50.csv')


# y llame a dos funciones que pongan su nombre en formato
# capitalizado 
def capitalizador(nombre):
    return nombre.capitalize()


# y calculen la letra de DNI correspondiente. 
def calcDNI(numero):

    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
               'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'] 
       
    resto = numero % 23 

    return letras[resto]



# Realiza la comprobación de rendimiento con la librería 
# cProfile y muestra los datos. Describe que indica cada 
# dato que nos proporciona cProfile.

