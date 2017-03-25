"""
Como pedido na videoaula desta semana, escreva um programa
que calcula as raízes de uma equação do segundo grau.
O programa deve receber os parâmetros a, b, e c da equação
ax2+bx+c, respectivamente, e imprimir o resultado na saída
da seguinte maneira:
Quando não houver raízes reais imprima:
    esta equação não possui raízes reais
    
Quando houver apenas uma raiz real imprima:
    a raiz desta equação é X

onde X é o valor da raiz. Quando houver duas raízes reais imprima:
    as raízes da equação são X e Y

onde X e Y são os valor das raízes.
Além disso, no caso de existirem 2 raízes reais, elas devem ser
impressas em ordem crescente, ou seja, X deve ser menor que Y.

Fórmula de Bháskara (Indiano que desenvolveu esta
equação) dada por: [-b +/- sqrt(Delta)]/2.a, onde delta
delta = (b)² - 4.a.c. Imprime na saída:
      i) delta < 0; não há raízes reais
     ii) delta = 0; Há somente uma raíz que é real.
    iii) delta > 0; Há duas raízes reais, que são: a e b
"""
import math

a = int(input("entre com o valor de a:"))
b = int(input("entre com o valor de b:"))
c = int(input("entre com o valor de c:"))

delta = (b**2 - 4*a*c)

if delta >= 0:
    raiz_não_negativa = True
    x1 = (- b + math.sqrt(delta))/(2*a)
    x2 = (- b - math.sqrt(delta))/(2*a)
    print(x1,x2)
    if x1 < x2:
        print("as raízes da equação são, x_1 = ",x1, "e x_2 = ",x2)
    elif x1 > x2:
        x1, x2 = x2, x1
        print(x1,x2)
        print("as raízes da equação são, x_1 = ",x1, "e x_2 = ",x2)
    else:
        raiz_não_negativa = True
        print("a raiz desta equação é", x1)
else:
    raiz_não_negativa = False
    raiz_não_real = "esta equação não possui raízes reais"
    print(raiz_não_real)
    
    
