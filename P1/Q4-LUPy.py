A = "[[5,-7,-10],[2,-4,5],[-9,1,-2]]"
b = [10,-4,8]


A = [i.split(",") for i in A[2:-2].split("],[")]
A = [[float(j) for j in i] for i in A]


print("\nSEU INPUTS:")
print("A = "+str(A))
print("b = "+str(b))

print("\n###################################################")

L = [[1 if j == k else 0 for j in range(len(A))] for k in range(len(A))]
n = 0

# Fazer o passo-a-passo a seguir len(A)-1 vezes
for i in range(len(A)-1):

    print("\n---Iteração "+str(n)+"---")
    n += 1

    # Definir matriz identidade P
    P = [[1 if j == k else 0 for j in range(len(A))] for k in range(len(A))]

    # Encontrar maior valor da coluna da iteração em A
    temp = abs(A[i][i])
    maior = i
    for j in range(i,len(A)):
        if abs(A[j][i]) > temp:
            temp = abs(A[j][i])
            maior = j

    # Trcar a linha desse valor pela linha da interação (em A, b e P)
    A[i],A[maior] = A[maior],A[i]
    b[i],b[maior] = b[maior],b[i]
    P[i],P[maior] = P[maior],P[i]
    L[i][:i], L[maior][:i] = L[maior][:i], L[i][:i]
    print("P = "+str(P))
    print("A("+str(n-1)+")' = "+str(A))

    # Dividir todas as colunas de A abaixo da coluna de iteração pelo valor da diagonal da iteração
    for j in range(i+1, len(A)):  # linhas abaixo do pivô
        L[j][i] = A[j][i] / A[i][i]
        
        for k in range(i, len(A)):  # colunas da linha
            A[j][k] = A[j][k] - L[j][i] * A[i][k]

    print("\nA("+str(n)+") = "+str(A))
    print("----------------------------------------")
    
# Definir U pela formula 
U = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    for j in range(len(A)):
        if j >= i:
            U[i][j] = A[i][j]

print("L = "+str(L))
print("U = "+str(U))

# Obter Y por L
Y = [0 for _ in range(len(A))]

for i in range(len(A)):
    soma = 0
    for j in range(i):
        soma += L[i][j] * Y[j]
    
    Y[i] = b[i] - soma

print("\nDado LY = b")
print("Y = "+str(Y))


# Obter X por U

X = [0 for _ in range(len(A))]

for i in range(len(A)-1, -1, -1):
    soma = 0
    for j in range(i+1, len(A)):
        soma += U[i][j] * X[j]
    
    X[i] = (Y[i] - soma) / U[i][i]

print("\nDado UX = Y")
print("X = "+str(X)+"\n")