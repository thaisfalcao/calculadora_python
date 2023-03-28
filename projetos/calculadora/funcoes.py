def soma(a,b):
  try:
    return float(a)+float(b)
  except ValueError:
    print(f"O input 'a' e 'b' devem ser uma string, recebido {a}: {type(a)} e {b}: {type(b)}")

def subtracao(a,b):
    return float(a)-float(b)

def multiplicacao(a,b):
  try:
    return float(a)*float(b)
  except ValueError:
    print(f"O input 'a' e 'b' devem ser uma string, recebido {a}: {type(a)} e {b}: {type(b)}")

def divisao(a,b):
    try:
        return float(a)/float(b)
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")