#PYTHON EXPORT Bissecao(f, e, a, b)

import sys
import math

f = sys.argv[0]
erro = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]

print("\nSEU INPUTS:")
print(f"função = {f}\nerro = {erro}\na = {a}\nb = {b}\n")

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

n = 0
while b - a > erro:
    print("##############################################\n")

    print(f"---Iteração {n}----\n")

    print(f"X{n} = ({a}+{b})/2 = {(a+b)/2}\n")

    x = (a+b)/2

    print("---Avaliando funções---\n")

    print(f"f(a) = {aval_funcao(f,a)}")
    print(f"f(b) = {aval_funcao(f,b)}")
    print(f"f(x{n}) = {aval_funcao(f,x)}\n")

    if aval_funcao(f,a)*aval_funcao(f,x) < 0:
        print(f"como f(a)*f(b) < 0, então b = x{n}")
        b = x
    else:
        print(f"como f(a)*f(b) > 0, então a = x{n}")
        a = x

    print(f"[{a},{b}]\n")
    
    n += 1
#end