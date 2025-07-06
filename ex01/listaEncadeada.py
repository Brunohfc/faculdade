from helper import HelperDados
from node import MeuNoCustomizado

validarDados = HelperDados()

class ListaEncadeada:
    
    def __init__(self):
        self.head = None


    def inserirHead(self, numero, cor):
        no = MeuNoCustomizado(numero=numero, cor=cor)
        #verificando se e instacancia do meu no
        if(isinstance(no, MeuNoCustomizado)):
            no.proximoNo = self.head
            self.head = no
            
    def imprimir(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.numero ," - " ,tmp.cor)
            
            tmp = tmp.proximoNo

    # ok- inserindo no final
    def inserirSemPrioridade(self, numero, cor):
        no = MeuNoCustomizado(numero=numero, cor = cor)
        #validado se o primeiro no esta vazi, adicionando caso esteja
        if(no == None):
            self.head = no
            return
        
        ultimo = self.head
        while ultimo.proximoNo != None:
            ultimo = ultimo.proximoNo

        ultimo.proximoNo = no

    def inserirComPrioridade(self, numero, cor):
        """
        Insere um novo nó na lista encadeada após todos os nós com cor 'amarelo' (A),
        mas sempre antes de qualquer nó com cor 'verde' (V).
        Se não houver nenhum nó verde, insere no final.
        """
        no = MeuNoCustomizado(numero=numero, cor=cor)
        # Se a lista estiver vazia, insere como head
        if self.head is None:
            self.head = no
            return

        atual = self.head
        anterior = None

        # Avança enquanto o próximo nó for amarelo
        while atual is not None and atual.cor == ValoresConstantes.AMARELO:
            anterior = atual
            atual = atual.proximoNo

        # Insere antes do primeiro nó verde ou após todos os amarelos
        if anterior is None:
            # Nenhum nó amarelo no início, insere como head
            no.proximoNo = self.head
            self.head = no
        else:
            no.proximoNo = atual
            anterior.proximoNo = no

    def inserir(self, numero, cor):
        """
        Insere um novo nó na lista encadeada.
        Se a cor for 'amarelo', insere no final.
        Se a cor for 'verde', insere antes de qualquer nó amarelo.
        """
        if validarDados.validarCor(cor):
            if cor == ValoresConstantes.AMARELO:
                self.inserirSemPrioridade(numero, cor)
            elif cor == ValoresConstantes.VERDE:
                self.inserirComPrioridade(numero, cor)

    def imprimirListaEspera(self):
        """
        Imprime os números e cores dos nós na lista encadeada.
        """
        tmp = self.head
        while tmp is not None:
            print(f"Número: {tmp.numero}, Cor: {tmp.cor}")
            tmp = tmp.proximoNo

    def atender(self):
        """
        Imprime os números e cores dos nós na lista encadeada,
        indicando que eles estão sendo atendidos.
        """
        tmp = self.head
        while tmp is not None:
            print(f"Atendendo - Número: {tmp.numero}, Cor: {tmp.cor}")
            tmp = tmp.proximoNo



class ValoresConstantes:
    AMARELO = "amarelo"
    VERDE = "verde"