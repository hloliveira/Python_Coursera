'''
    Curso de Programação Introdução à Linguagem Python
    Professor Ministrante: Fabio Kon - IME/USP
    MOOC - COURSERA
    Programa que receba quatro notas, calcule e imprima
    a média aritmética.
 ==> Tarefa de programação: Lista de exercícios - 1
'''

#Entrada de dados

nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
nota4 = int(input("Digite a quarta nota:"))

#Cálculo da média aritmética
media = (nota1 + nota2 + nota3 + nota4)/4

#Saída de dados
print("A média aritmética é",media)
