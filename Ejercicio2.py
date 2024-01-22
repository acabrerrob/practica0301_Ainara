# Escribir una función que lea dos ficheros csv con una
# lista larga de datos de personas (50 personas y 1000 personas)
import csv, cProfile


def capitalizador(nombre):
    """Función que recibe una string y devuelve la string capitalizada.
        - Parámetro: nombre = string de nombre completo.
        - Salida = string de nombre completo capitalizado.
    """
    return str(nombre.capitalize())


def calcDNI(numero):
    """Función que recibe un número entero positivo y devuelve 
        el mismo número seguido de la letra correspondiente.
        - Parámetro: numero = número de DNI.
        - Salida = número del DNI con su correspondiente letra.
    """

    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
               'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'] 
    
    return f'{numero}{letras[numero % 23]}'



def lectorDoc(archivo):
    """Función que recibe el nombre de un archivo en formato string,
        lo lee y lo copia a un archivo nuevo.
        - Parámetro: archivo = fichero tipo csv en formato string.
        - Salida = al no tener return no devuelve nada pero, crea
            un archivo nuevo con los datos del antiguo archivo pero
            incluyendo las modificaciones.
    """
    with open (archivo , 'r') as file :    #función 1
        with open ('archivoNuevo.csv', 'w') as file2:
            
            for i in (file.readlines()):
                nombre, numero = i.split(',')
                file2.write(capitalizador(nombre) + ', ' + calcDNI(int(numero)) + '\n')



# Posibles llamadas:

# cProfile.run("lectorDoc('50.csv')")
# lectorDoc('50.csv')

# cProfile.run("lectorDoc('1000.csv')")
# lectorDoc('1000.csv')