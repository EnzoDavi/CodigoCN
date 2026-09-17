a = 3
b = 9
funct = "ln(5*x-3)"
m = 12

import math

h = (b-a)/m

print("##### Aproximando a integral #####\n")

def aval_funcao(fun, x):
    fun = fun.upper()
    
    fun = fun.replace('SEN', 'math.sin')
    fun = fun.replace('COS', 'math.cos')
    fun = fun.replace('TAN', 'math.tan')
    fun = fun.replace('E^', 'math.exp')
    fun = fun.replace('LN', 'math.log')
    fun = fun.replace('^', '**')
    
    fun = fun.replace('X', f'({x})')
    
    return eval(fun, {"math": math})

X = [a+h*i for i in range(m+1)]
f = [aval_funcao(funct,Xi) for Xi in X]

valor = (h/3)*(f[0] + f[-1] + 4*sum([f[i] for i in range(m) if i % 2 == 1]) + 2*sum([f[i] for i in range(1,m) if i % 2 == 0]))

print("I = (h/3)*(f(X0) + f(Xm) + 4*SomaImpares(f(Xi)) + 2*SomaPares(f(Xi))) = " + str(valor))

print("\n##### Calculando erro da função #####\n")

def quarta_derivada(func, x, h=1e-2):
    f_menos2 = aval_funcao(func, x - 2 * h)
    f_menos1 = aval_funcao(func, x - h)
    f_zero = aval_funcao(func, x)
    f_mais1 = aval_funcao(func, x + h)
    f_mais2 = aval_funcao(func, x + 2 * h)
    return (f_menos2 - 4 * f_menos1 + 6 * f_zero - 4 * f_mais1 + f_mais2) / (h ** 4)


def modulo_quarta_derivada(func, x, h=1e-2):
    return abs(quarta_derivada(func, x, h))


def maximo_quarta_derivada(func, a, b, passos=2000, h=1e-2, refinamentos=60):
    melhor_x = a
    melhor_valor = modulo_quarta_derivada(func, a, h)
    delta = (b - a) / passos

    for i in range(1, passos + 1):
        x = a + i * delta
        try:
            valor = modulo_quarta_derivada(func, x, h)
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
        fc = modulo_quarta_derivada(func, c, h)
        fd = modulo_quarta_derivada(func, d, h)
        if fc > fd:
            direita = d
        else:
            esquerda = c
        c = direita - razao_aurea * (direita - esquerda)
        d = esquerda + razao_aurea * (direita - esquerda)

    x_max = (esquerda + direita) / 2
    valor_max = modulo_quarta_derivada(func, x_max, h)
    return x_max, valor_max

x_max, valor_max = maximo_quarta_derivada(funct, a, b)

e = ((b-a)*valor_max*h**4)/180

print("erro = ((b-a)*max|f''''(x)|*h^4)/180 = " + str(e))
