"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    for i in range(0, n+1):
        resultado = i + i
        return resultado
print(suma_ciclo(5))


def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    pass
