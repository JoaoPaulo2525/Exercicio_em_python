import math
import os

#Função narrativa
nome = input("Digite seu nome: ")

#Função do tamanho da narrativa
tam_nome = len(nome)

#Função da biblioteca math
numero = float(input("Digite um numero: "))
raiz = math.sqrt(numero)

print(f"Olá {nome}, o tamanho do seu nome é {tam_nome} caracteres e a raiz quadrada de {numero} é {raiz}.")

#Lista de numeros
List = [10, 15, 20, 25, 30]
numero = len(List)
soma = sum(List)
print(f"A lista contém {numero} elementos e a soma dos elementos é {soma}. ")



