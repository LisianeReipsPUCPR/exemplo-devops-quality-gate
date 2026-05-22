def somar(a, b):
    return a + b

#def dividir(a, b):
    # BUG intencional: sem tratamento de divisão por zero
#    return a / b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro")
    return a / b
