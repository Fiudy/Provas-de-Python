
numeros_pares = []
numeros_impares = []


for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)


tupla_numeros = (numeros_pares, numeros_impares)


quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)


print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Números em uma tupla:", tupla_numeros)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma de números pares:", soma_pares)
print("Soma de números ímpares:", soma_impares)
