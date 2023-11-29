def calcular_media(notas):
   return sum(notas) / len(notas)

def verificar_situacao(media):
   if media < 7:
       return "Reprovado"
   elif media >= 7 and media < 10:
       return "Aprovado"
   else:
       return "Parabéns, sua média é 10"


notas = []
while True:
   nota = input("Digite uma nota (ou 'sair' para terminar): ")
   if nota.lower() == 'sair':
       break
   notas.append(float(nota))

# Calcula a média das notas
media = calcular_media(notas)

# Determina a situação do aluno
situacao = verificar_situacao(media)

# Exibe a situação do aluno
print("A média do aluno é", media)
print("A situação do aluno é", situacao)
