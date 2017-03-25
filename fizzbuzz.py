"""  FizzBuzz parcial - parte1
Código que recebe um número inteiro na entrada e imprime
FizzBuzz - na saída quando o número for divisível por 3 e por 5.
Caso contrário, imprime o mesmo o número que foi dado na entrada.
"""

x = int(input("Entre com um número:"))

if ((x%3) == 0 and (x%5) == 0):
    print("FizzBuzz")
else:
    print(x)
