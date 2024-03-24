from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input("Qual a largura do comodo:"),
    input("Qual a profundidade do comodo:")
)

# calc.area_paredes: float = 2 * (largura * profundidade) * altura

print("A area das paredes é :", calc.calcular_area_paredes(comodo))


print("A area do teto é :",calc.calcular_area_teto(comodo))

print("A litragem necessaria é :", calc.calcular_litragem)
