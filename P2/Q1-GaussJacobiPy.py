A = [[4,-2,1],[-2,3,4],[1,-2,10]]
b = [2,-3,4]
e = 0.1
x = [-1,0,0.5]

print("\nSEU INPUTS: ")
print("A = "+str(A)+"\nb = "+str(b)+"\ne = "+str(e)+"\nx = "+str(x))
print("\n######################################\n")


for i in range(len(A)):
    print("X"+str(i+1)+"(k+1) = " + " + ".join(["("+str(-1*A[i][j]/A[i][i])+")"+"*X"+str(j+1) for j in range(len(A)) if i != j]) + " + ("+str(b[i]/A[i][i])+")")

print("\n#######################################\n")

n = 0
print("---Iteração "+str(n)+"---\n")
n += 1

def erro_matriz(k, kDec1):
    Max = abs(k[0]-kDec1[0])
    for i in range(1,len(k)):
        if abs(k[i]-kDec1[i]) > Max:
            Max = abs(k[i]-kDec1[i])
    return Max/max([abs(j) for j in k])
    
xSum1 = []
for i in range(len(A)):
    xSum1.append(b[i]/A[i][i] + sum([-1*A[i][j]*x[j]/A[i][i] if i != j else 0 for j in range(len(A))]))
print(xSum1)    
    
while erro_matriz(xSum1,x) > e:
    x = xSum1
    xSum1 = []
    for i in range(len(A)):
        xSum1.append(b[i]/A[i][i] + sum([-1*A[i][j]*x[j]/A[i][i] if i != j else 0 for j in range(len(A))]))
    print("---Iteração "+str(n)+"---\n")
    n += 1
    print("X = "+str(xSum1)+"\n")