def soma(a,b):
  try:
    return a+b
  except TypeError:
    print(f"O input 'a' e 'b' devem ser uma string, recebido {a}: {type(a)} e {b}: {type(b)}")
