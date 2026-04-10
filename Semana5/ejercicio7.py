"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    total = 0
    for ahorro in ahorros:
        total = total + ahorro
    return total
print(ahorro_total_ciclo([100, 200, 300, 400]))


def ahorro_total_recursivo(ahorros):
    if len(ahorros) == 0:
        return 0
    else:
        return ahorros [0] + ahorro_total_recursivo(ahorros[1:])
print(ahorro_total_recursivo([100,200,300,400]))
