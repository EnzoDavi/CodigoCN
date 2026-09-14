import math

f = "2*SEN(x)-x^3*e^x-4*x^2+2"
erro = 0.01
a = 0.5
b = 0.8

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
        print(f"como f(a)*f(x) < 0, então b = x{n}")
        b = x
    else:
        print(f"como f(a)*f(x) > 0, então a = x{n}")
        a = x

    print(f"[{a},{b}]\n")
    
    n += 1