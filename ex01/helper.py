from node import MeuNoCustomizado


class HelperDados:

    def validarInstancia(obj, Instancia):
        if(isinstance(obj, MeuNoCustomizado)):
            return True
        else:
            return False