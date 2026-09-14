X = [3,3.2,3.4]
f = [20.08,24.53,29.96]
x0 = 3.3

import math

def lagrange(x_vals, y_vals, x):
    n = len(x_vals)
    resultado = 0

    for i in range(n):
        termo = y_vals[i]
        for j in range(n):
            if i != j:
                termo *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        resultado += termo

    return resultado


def erro_interpolacao_exp(x_vals, x):
    """
    Calcula o limitante do erro para f(x) = e^x
    usando interpolação de grau n-1
    """
    n = len(x_vals)

    # produto (x - xi)
    produto = 1
    for xi in x_vals:
        produto *= (x - xi)

    # máximo de e^x no intervalo
    max_x = max(x_vals + [x])
    M = math.exp(max_x)

    erro = abs(M * produto / math.factorial(n))
    return erro

print(lagrange(X,f,x0))
print(erro_interpolacao_exp(X,x0))