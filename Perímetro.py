''' Programa para calcular o perímetro e a área de um quadrado
    de lado "l"
    Tarefa de programação: Lista de exercícios - 1
    Curso de Introdução ao Python - IME/USP
'''
#entrada de dados

lado = int(input("Digite o valor correspondente ao lado de um quadrado:"))

perímetro = lado + lado + lado + lado
área = lado**2

#saida de dados
#obsoleta
#print ( 'perimetro:%d - área: %d' %(perímetro, área))

print ("perímetro:", perímetro, "área:", área)