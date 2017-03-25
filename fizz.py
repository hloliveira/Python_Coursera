"""  FizzBuzz parcial - parte1
Código que recebe um número inteiro na entrada e imprime
Fizz - quando o número for divisível por 3. Caso contrário,
imprime o mesmo o número que foi dado na entrada.
"""

x = int(input("Entre com um número:"))

if ((x%3) == 0):
    print("Fizz")
else:
    print(x)
