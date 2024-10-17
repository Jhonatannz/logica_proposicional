# Función para imprimir la tabla de verdad de la compuerta AND
def tabla_verdad_and():
    print("A | B | A AND B")
    print("---------------")
    # Posibles combinaciones de A y B
    combinaciones = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    # Evaluación de la compuerta AND
    for A, B in combinaciones:
        resultado = A and B
        print(f"{A} | {B} |   {resultado}")

# Llamada a la función
tabla_verdad_and()
