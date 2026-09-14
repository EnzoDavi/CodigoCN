#PYTHON EXPORT MNR(a,b,c,d)

import sys
import math

f = sys.argv[0]
e = float(sys.argv[1])
x0 = float(sys.argv[2])

print("\nSEU INPUTS:")
print("função = "+str(f)+"\nerro = "+str(e)+"\nX0 = "+str(x0)+"\n")

print("OBS: Por motivos tecnicos esse código não consegue imprimir diretamente o phi(x), mas o valor do mesmo usado é dado por: phi(x) = x - f(x)/f'(x)\n")

def aval_funcao(fun, x):
    fun = fun.upper()
    
    fun = fun.replace('SEN', 'math.sin')
    fun = fun.replace('COS', 'math.cos')
    fun = fun.replace('TAN', 'math.tan')
    fun = fun.replace('E^', 'math.exp')
    fun = fun.replace('LN', 'math.log')
    fun = fun.replace('^', '**')
    
    fun = fun.replace('X', "("+str(x)+")")
    
    return eval(fun, {"math": math})

def diff(funcao, valor):
    return ((aval_funcao(funcao, valor+1e-6) - aval_funcao(funcao, valor-1e-6)) / (2*1e-6))

n = 0
while abs(aval_funcao(f,x0)) > e:
    print('#######################################################\n')
    print("---Iteração "+str(n)+"---\n")
    x0 = x0 - (aval_funcao(f,x0)/diff(f,x0))
    print("x"+str(n)+" = "+str(x0))
    print("f(x"+str(n)+") = "+str(aval_funcao(f,x0))+"\n")
    n += 1