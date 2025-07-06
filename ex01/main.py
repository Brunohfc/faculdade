from listaEncadeada import ListaEncadeada, MeuNoCustomizado


def menu():
    while True:
        print("1 - Inserir no início (head)")
        print("2 - Inserir sem prioridade")
        print("3 - Inserir com prioridade")
        print("4 - Imprimir lista")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao in ["1", "2", "3", "4", "5"]:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    
    lista = ListaEncadeada()

    while True:
        opcao = menu()

        if opcao == "1":
            numero = input("Digite o número: ")
            cor = input("Digite a cor (A, V): ")
            lista.inserirHead(numero, cor)
        elif opcao == "2":
            numero = input("Digite o número: ")
            cor = input("Digite a cor (A, V): ")
            lista.inserirSemPrioridade(numero, cor)
        elif opcao == "3":
            numero = input("Digite o número: ")
            cor = input("Digite a cor (A, V): ")
            lista.inserirComPrioridade(numero, cor)
        elif opcao == "4":
            lista.imprimir()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
