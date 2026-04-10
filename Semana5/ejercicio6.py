"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    resultado = 0
    for venta in ventas:
        resultado = resultado + venta
    return resultado
print(total_ventas_ciclo([100, 200, 300]))    



def total_ventas_recursivo(ventas):
    if not ventas:
        return 0
    else:
        return ventas[0] + total_ventas_ciclo(ventas[1:])
print(total_ventas_recursivo([100, 200, 300]))
