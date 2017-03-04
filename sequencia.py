'''
  Programa que calcula a soma de uma sequencia de números a partir
  de uma lista. O programa pára quando encontra um zero na lista.
  Versão com o comando for
'''

def sequencia2():
    lista = [17,12,4,-6,8,0, 9,11]
    soma = 0

    for i in lista:
        if i == 0:
            break
        soma = soma + i
    print ("A soma é", soma)

#----------------------------------------------
#sequencia2()

'''
  Versão dois do programa que calcula a soma de uma sequencia de
  números a partir de dados digitados na tela. Nessa versão foi
  utilizado o comando while
'''

def sequencia():
    num = int(input("Entre com um número:"))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Entre com um número:"))
    print ("A soma é", soma)

sequencia()