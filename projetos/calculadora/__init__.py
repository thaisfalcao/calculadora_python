from funcoes import soma
from funcoes import subtracao
from funcoes import multiplicacao
from funcoes import divisao

def calcule():
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação desejada: ")
    if operacao == "soma" or operacao == "+":
        return soma(n1,n2)
    elif operacao == "subtração" or operacao == "-":
        return subtracao(n1,n2)
    elif operacao == "multiplicação" or operacao == "*":
        return multiplicacao(n1,n2)
    elif operacao == "divisão" or operacao == "/":
        return divisao(n1,n2)
    else:
        print("Operação inválida")