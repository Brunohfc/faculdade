
class No:
    def __init__(self, sigla: str, estado: str):
        self.sigla = sigla
        self.estado = estado
        self.proximo = None


class Table:
    def __init__(self, tamanhoTable: int = 10):
        self.tamanhoTable = tamanhoTable
        self.tabela = [None] * tamanhoTable

    def _hash(self, sigla):
        return hash(sigla) % self.tamanhoTable
    
    def inserir(self, sigla, estado):
        # fazendo o hash e criando um novo nó
        indice = self._hash(sigla)
        no = No(sigla, estado)

        # adicionando o nó
        no.proximo = self.tabela[indice]
        self.tabela[indice] = no
       

    def buscar(self, sigla):
        indice = self._hash(sigla)
        atual = self.tabela[indice]
        while atual is not None:
            if atual.sigla == sigla:
                return atual.estado
            atual = atual.proximo
        return None
    
    def tamanhoTabela(self):
        return self.tamanhoTable
    
    def imprimir(self, arrow=" -> "):
        for i in range(self.tamanhoTable):
            atual = self.tabela[i]
            if atual is not None:
                print(f"Índice {i}: ", end="")
                siglasEstados = []
                while atual is not None:
                    siglasEstados.append(f"{atual.sigla} ({atual.estado})")
                    print(" -> ".join(siglasEstados) + " -> None")
                    atual = atual.proximo
                print("None")
            else:
                print(f"Índice {i}: None")

    def printar_tabela(self):
        for i, head in enumerate(self.tabela):
            print(f"Índice {i}:", end=" ")
            if not head:
                print("None")
            else:
                curr = head
                siglas = []
                while curr:
                    siglas.append(curr.sigla)
                    curr = curr.proximo
                print(" -> ".join(siglas) + " -> None")