from listaEncadeada import ListaEncadeada


if __name__ == "__main__":
    minhaLista = ListaEncadeada()
    print("adicionando A")
    minhaLista.inserirHead(1,"verde")
    minhaLista.inserirSemPrioridade(0,"amarelo")
    minhaLista.inserirHead(2,"verde")
    minhaLista.inserirHead(3,"verde")
    
    minhaLista.imprimir()