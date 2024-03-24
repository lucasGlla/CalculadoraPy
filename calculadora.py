class Calculadora:
    __area_paredes : float
    __area_teto : float


    def calcular_area_paredes(self,comodo):
        self.__area_paredes = 2 * (comodo.__largura * comodo.__profundidade) * comodo.__altura
        return self.__area_paredes
    def calcular_area_teto(self,comodo):
        self.__area_teto = comodo.__largura * comodo.__profundidade
        return self.__area_teto
    def calcular_litragem(self):
        if self.__area_paredes <= 0 or self.__area_teto <= 0:
            print('Não é possivel calcular a litragem com os valores informados')
            exit()
        return (self.__area_paredes + self.__area_teto) / 10