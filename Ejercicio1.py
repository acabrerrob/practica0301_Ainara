def fibonacciBucle(n):
    '''
    Función que recibe u número entero positivo n 
    y calcula el número de fibonacci asociado a ese número.
   
    - Parámetro = n: número entero positivo.
    - Salida: número de fibonacci asociado al parámetro n introducido.
  
    '''
    a = 0
    b = 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for index in range(n-1):
            c = a + b
            a = b
            b = c
        return c



# Escribir dos funciones, una función que reciba un 
# número entero positivo n y calcule el número de 
# fibonacci asociado a ese número de manera recursiva 
# y otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de 
# ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.

def fibonacciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
print(fibonacciRecursive(3))