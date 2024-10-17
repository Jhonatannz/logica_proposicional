# Función para la compuerta bicondicional (↔)
def bicondicional(a, b):
    return a == b

# Imprimir tabla de verdad
print("A | B | A ↔ B")
print("----------------")
valores = [True, False]
for a in valores:
    for b in valores:
        resultado = bicondicional(a, b)
        print(f"{a} | {b} |  {resultado}")
