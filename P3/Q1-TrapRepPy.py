a = 3
b = 7
erro = 0.00001
funct = "exp(6-x)"

import math

def aval_função(func, x):
    contexto = {nome: obj for nome, obj in math.__dict__.items() if not nome.startswith("_")}
    contexto["x"] = x
    return eval(func, {"__builtins__": {}}, contexto)


def segunda_derivada(func, x, h=1e-4):
    f_mais = aval_função(func, x + h)
    f_zero = aval_função(func, x)
    f_menos = aval_função(func, x - h)
    return (f_mais - 2 * f_zero + f_menos) / (h ** 2)


def modulo_segunda_derivada(func, x, h=1e-4):
    return abs(segunda_derivada(func, x, h))


def maximo_segunda_derivada(func, a, b, passos=2000, h=1e-4, refinamentos=60):
    melhor_x = a
    melhor_valor = modulo_segunda_derivada(func, a, h)
    delta = (b - a) / passos

    for i in range(1, passos + 1):
        x = a + i * delta
        try:
            valor = modulo_segunda_derivada(func, x, h)
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_x = x

    esquerda = max(a, melhor_x - delta)
    direita = min(b, melhor_x + delta)
    razao_aurea = (math.sqrt(5) - 1) / 2

    c = direita - razao_aurea * (direita - esquerda)
    d = esquerda + razao_aurea * (direita - esquerda)

    for _ in range(refinamentos):
        fc = modulo_segunda_derivada(func, c, h)
        fd = modulo_segunda_derivada(func, d, h)
        if fc > fd:
            direita = d
        else:
            esquerda = c
        c = direita - razao_aurea * (direita - esquerda)
        d = esquerda + razao_aurea * (direita - esquerda)

    x_max = (esquerda + direita) / 2
    valor_max = modulo_segunda_derivada(func, x_max, h)
    return x_max, valor_max

x_max, valor_max = maximo_segunda_derivada(funct, a, b)
n = math.ceil(math.sqrt((((b-a)**3)*valor_max)/(12*erro)))

print("n = arredonda.para.cima(sqrt(((b-a)^3*max|f''(x)|)/(12*erro))) = " + str(n))
