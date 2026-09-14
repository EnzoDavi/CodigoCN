#PYTHON EXPORT LU(a,b,c,d)

import sys

A = sys.argv[0]
b = sys.argv[1]

print("\nSEU INPUTS:")
print("A = "+str(A))
print("b = "+str(b))

A = [i.split(",") for i in A[2:-2].split("],[")]
A = [[float(j.replace('\u2212','-')) for j in i] for i in A]

b = [float(j.replace('\u2212','-')) for j in b[2:-2].split("],[")]

print("\n###################################################")

L = [[1 if j == k else 0 for j in range(len(A))] for k in range(len(A))]
n = 0

for i in range(len(A)-1):

    print("\n---Iteração "+str(n)+"---")
    n += 1

    P = [[1 if j == k else 0 for j in range(len(A))] for k in range(len(A))]

    temp = abs(A[i][i])
    maior = i
    for j in range(i,len(A)):
        if abs(A[j][i]) > temp:
            temp = abs(A[j][i])
            maior = j

    A[i],A[maior] = A[maior],A[i]
    b[i],b[maior] = b[maior],b[i]
    P[i],P[maior] = P[maior],P[i]
    L[i][:i], L[maior][:i] = L[maior][:i], L[i][:i]
    print("P = "+str(P))
    print("A("+str(n-1)+")' = "+str(A))

    for j in range(i+1, len(A)):  # linhas abaixo do pivô
        L[j][i] = A[j][i] / A[i][i]
        
        for k in range(i, len(A)):  # colunas da linha
            A[j][k] = A[j][k] - L[j][i] * A[i][k]

    print("\nA("+str(n)+") = "+str(A))
    print("---------------------------------------")
    
U = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    for j in range(len(A)):
        if j >= i:
            U[i][j] = A[i][j]

print("L = "+str(L))
print("U = "+str(U))

Y = [0 for _ in range(len(A))]

for i in range(len(A)):
    soma = 0
    for j in range(i):
        soma += L[i][j] * Y[j]
    
    Y[i] = b[i] - soma

print("\nDado LY = b")
print("Y = "+str(Y))

X = [0 for _ in range(len(A))]

for i in range(len(A)-1, -1, -1):
    soma = 0
    for j in range(i+1, len(A)):
        soma += U[i][j] * X[j]
    
    X[i] = (Y[i] - soma) / U[i][i]

print("\nDado UX = Y")
print("X = "+str(X)+"\n")