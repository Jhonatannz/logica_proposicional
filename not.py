# Función para la compuerta NOT
def not_gate(input_value):
    return not input_value

# Imprimir la tabla de verdad de la compuerta NOT
print("Tabla de Verdad de la Compuerta NOT")
print("---------------------------")
print("| Entrada | Salida |")
print("---------------------------")
for input_value in [True, False]:
    output_value = not_gate(input_value)
    print(f"|   {input_value}   |   {output_value}  |")
print("---------------------------")
