"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    resultado = 0
    for i in range (1,n+1):
        if i % 2 == 0:
            resultado = resultado + 1
    return resultado
print(contar_pares_ciclo(6))

def contar_pares_recursivo(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return 1 + contar_pares_recursivo(n-1)
    else:
        0 + contar_pares_recursivo(n-1)
print(contar_pares_recursivo(6))
    
