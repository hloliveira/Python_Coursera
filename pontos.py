"""  FizzBuzz parcial - parte1
Receba 4 números inteiros na entrada. Os dois primeiros devem
corresponder, respectivamente, às coordenadas x e y de um ponto
em um plano cartesiano. Os dois últimos devem corresponder,
respectivamente, às coordenadas x e y de um outro ponto no mesmo
plano.
Calcule a distância entre os dois pontos. Se a distância for
maior ou igual a 10, imprime: "longe" na saída. Caso contrário,
quando a distância for menor que 10, imprime: "perto".  
"""
import math

x1 = int(input("Entre com a coordenada x1:"))
y1 = int(input("Entre com a coordenada y1:"))
x2 = int(input("Entre com a coordenada x2:"))
y2 = int(input("Entre com a coordenada y2:"))

D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if (D >= 10):
    print("longe")
else:
    print("perto")
