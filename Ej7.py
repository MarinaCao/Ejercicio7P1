# Solicitar al usuario que ingrese una lista de números enteros separados por espacios
numeros_str = input("Ingrese una lista de números enteros separados por espacios: ")

# Convertir la cadena de entrada en una lista de números enteros
numeros = list(map(int, numeros_str.split()))

# Filtrar los números que no son múltiplos de 3 y convertirlos en cadenas
numeros_filtrados = [str(numero) for numero in numeros if numero % 3 != 0]

# Unir los números filtrados en una sola cadena separada por guiones
cadena_final = "-".join(numeros_filtrados)

# Imprimir la cadena final
print("Cadena final excluyendo los números múltiplos de 3:", cadena_final)
