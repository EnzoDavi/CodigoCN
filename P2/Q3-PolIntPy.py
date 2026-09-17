import math

X = [0.9,1,1.3,1.8,2,2.2]
f = [-0.105,0,0.262,0.588,0.693,0.788]
x0 = 1.4
ordem = 3

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

print("\n###### Tebela diferença divisão ######\n")

dif_div = [f]

for i in range(len(X)-1):
    dif_div.append([])
    for j in range(len(X)-1-i):
        dif_div[-1].append((dif_div[-2][j+1]-dif_div[-2][j])/(X[j+i+1]-X[j]))

for i in dif_div:
    print(i)

print("\n##### Definir polinomio de Newton #####\n")

for i in range(len(X)):
    if x0 < X[i]:
        ponto_ref = i
        break

polinomioN = "P(x) = "

for i in range(ordem):
    polinomioN += str(dif_div[i][ponto_ref-ordem+1])
    polinomioN += "*"
    for j in range(i):
        polinomioN += ("(x - ")
        polinomioN += str(X[ponto_ref-ordem+j+1])
        polinomioN += ")*"
    polinomioN = polinomioN[:-1]
    polinomioN += " + "

polinomioN = polinomioN[:-3]

print(polinomioN)

print("\n##### Calculando função em X0 #####\n")

valor = aval_funcao(polinomioN[6:],x0)

print("P(" + str(x0) + ") = " + str(valor))

print("\n##### Calculando o erro #####\n")

erro = dif_div[ordem][ponto_ref-ordem]
texto = "erro = " + str(dif_div[ordem][ponto_ref-ordem])

for i in range(ordem):
    erro *= x0-X[ponto_ref-i]
    texto += "(" + str(x0) + " - " + str(X[ponto_ref-i]) + ")"

print(texto + " = " + str(abs(erro)))