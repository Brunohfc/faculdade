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

