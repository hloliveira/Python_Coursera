"""
Este programa calcula as raízes de um polinômio de segundo grau
utilizando a fórmula de Bháskara (Indiano que desenvolveu esta
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

x1 = (- b + math.sqrt(delta))/(2*a)
x2 = (- b - math.sqrt(delta))/(2*a)

if delta > 0:
    raiz_não_negativa = True
    print("há duas raízes reais, que são, x_1 = ",x1, "e x_2 = ",x2)
elif delta == 0:
    raiz_não_negativa = True
    print("há somente uma raiz real, x_1 = x_2 =",x1)
else:
    raiz_não_negativa = True
    raiz_não_real = "Não há raízes Reais!!!"
    print(raiz_não_real)
    
    
