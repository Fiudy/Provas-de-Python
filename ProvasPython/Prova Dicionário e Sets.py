alunos = {} 

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar um aluno")
    print("2. Remover um aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        alunos[matricula] = nome
        print(f"Aluno {nome} com matrícula {matricula} adicionado com sucesso!")

    elif opcao == "2":
        matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
        if matricula in alunos:
            nome = alunos.pop(matricula)
            print(f"Aluno {nome} com matrícula {matricula} removido com sucesso!")
        else:
            print("Número de matrícula não encontrado. Nenhum aluno removido.")

    elif opcao == "3":
        if len(alunos) > 0:
            print("Lista de alunos:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula}, Nome: {nome}")
        else:
            print("Nenhum aluno registrado.")

    elif opcao == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
