# Escribir dos funciones, una función que reciba un 
# número entero positivo n y calcule el número de 
# fibonacci asociado a ese número de manera recursiva 
# y otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de 
# ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.
def fibonacciBucle(n):
    '''
    
    
    '''
    a = 0
    b = 1
    count = 2


    if n == 0:
        print('Su posición corresponde a: 0')
    elif n == 1:
        print('Su posición corresponde a: 1')
    else:
        for i in range (n-1):
            c = a + b
            c <= n    
            a = b
            b = c
            count += 1

        print(f'Su posición corresponde a: {count}')






        
fibonacciBucle(1)