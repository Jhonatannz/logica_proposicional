# Función para calcular la implicación lógica
def implicacion(p, q):
    return not p or q

# Valores posibles de P y Q
valores = [(False, False), (False, True), (True, False), (True, True)]

# Imprimir la tabla de verdad
print(" P    Q   P → Q")
print("-----------------")
for p, q in valores:
    resultado = implicacion(p, q)
    print(f"{p}  {q}   {resultado}")
