# Función para imprimir la tabla de verdad de la compuerta OR
def tabla_verdad_or():
    print("A | B | A OR B")
    print("-" * 15)
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A or B
            print(f"{A} | {B} |   {resultado}")

# Llamamos a la función para mostrar la tabla de verdad
tabla_verdad_or()
