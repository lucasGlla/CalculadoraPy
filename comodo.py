class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self,largura,profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__largura
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def altura(self):
        return self.__altura
    
    @largura_setter
    def largura(self,largura):
        try:
            self.largura = float(largura)
        except Exception:
            print('O valor da largura é invalido')
            exit()
    
    @profundidade_setter
    def profundidade(self,profundidade):
        try:
            self.profundidade = float(profundidade)
        except Exception:
            print('O valor da profundidade é invalido')
            exit()