"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado = resultado * base 
    return resultado
print(potencia_ciclo(4, 6))

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)
print(potencia_ciclo(4, 6))
