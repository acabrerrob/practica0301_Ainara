import datetime

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
    
start_time = datetime.datetime.now()

fibonacciBucle(40)

end_time = datetime.datetime.now()

print('El tiempo de ejecución es:', end_time - start_time)


def fibonacciRecursive(n):
    '''
    Función que recibe u número entero positivo n 
    y calcula el número de fibonacci asociado a ese número.
   
    - Parámetro = n: número entero positivo.
    - Salida: número de fibonacci asociado al parámetro n introducido.
  
    '''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

start_time = datetime.datetime.now()

fibonacciRecursive(40)

end_time = datetime.datetime.now()

print('El tiempo de ejecución es:', end_time - start_time)