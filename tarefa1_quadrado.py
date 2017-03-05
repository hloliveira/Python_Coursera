'''
    Curso de Programação Introdução à Linguagem Python
    Professor Ministrante: Fabio Kon - IME/USP
    MOOC - COURSERA
    Programa para calcular o perímetro e a área de um
    quadrado de lado "l"
 ==> Tarefa de programação: Lista de exercícios - 1
'''

#Entrada de dados

lado = int(input("Digite o valor correspondente ao lado de um quadrado:"))

#Cálculo do perímetro
perimetro = lado + lado + lado + lado # tb possível 4*lado

#Cálculo da área
área = lado**2

#Saída de dados
print("perímetro:",perimetro,"- área:",área)
