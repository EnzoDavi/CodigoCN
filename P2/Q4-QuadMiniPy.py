x = [0, 0.5, 1.0, 2.5, 3.0]
y = [2.0, 2.6, 3.7, 13.2, 21.0]

a = 1.2

import math

def ajuste_exponencial(x, y, a):
    # Transformação
    Y = [math.log(y[i] - a) for i in range(len(y))]

    n = len(x)
    
    # Somatórios
    Sx = sum(x)
    Sy = sum(Y)
    Sxx = sum(xi**2 for xi in x)
    Sxy = sum(x[i]*Y[i] for i in range(n))

    # Resolver sistema normal (reta)
    c = (n*Sxy - Sx*Sy) / (n*Sxx - Sx**2)
    A = (Sy - c*Sx) / n

    # Recuperar b
    b = math.exp(A)

    return b, c


def modelo(x, a, b, c):
    return a + b * math.exp(c * x)

b, c = ajuste_exponencial(x, y, a)

print("b =", b)
print("c =", c)

# Teste do modelo
for xi in x:
    print(f"x={xi}, y_aprox={modelo(xi, a, b, c)}")