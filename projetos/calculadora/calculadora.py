from funcoes import *

def calcule():
    n1 = input("Digite o primeiro número: ")
    print(n1)
    n2 = input("Digite o segundo número: ")
    print(n2)
    operacao = input("Digite a operação desejada: ")
    print(operacao)
    if operacao == "soma" or operacao == "+":
        print(soma(n1,n2))
    elif operacao == "subtração" or operacao == "-":
        print(subtracao(n1,n2))
    elif operacao == "multiplicação" or operacao == "*":
        print(multiplicacao(n1,n2))
    elif operacao == "divisão" or operacao == "/":
        print(divisao(n1,n2))
    else:
        print("Operação inválida")
