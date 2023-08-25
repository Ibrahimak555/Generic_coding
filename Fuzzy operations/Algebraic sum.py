A=dict()
B=dict()
C=dict()

A={10:0.0, 20:0.3, 30:0.9, 40:0.2, 50:0.5, 60:0.2}
B={10:0.4, 20:1.0, 30:0.0, 40:0.5, 50:0.8, 60:0.1}

for i in A:
    C[i] = A[i] + B[i] - (A[i]*B[i])

c=0
print("A = {",end='')
for i in A:
    c = c+1
    if c < len(A):
        print("{"+str(i)+"/"+str(A[i])+"}",end=",")
    else:
        print("{"+str(i)+"/"+str(A[i])+"}",end="")
print("}")

print("B = {",end='')
c=0
for i in B:
    c = c+1
    if c < len(B):
        print("{"+str(i)+"/"+str(B[i])+"}",end=",")
    else:
        print("{"+str(i)+"/"+str(B[i])+"}",end="")
print("}")

print("A + B = {",end='')
c=0
for i in C:
    c = c+1
    if c < len(C):
        print("{"+str(i)+"/"+str(C[i])+"}",end=",")
    else:
        print("{"+str(i)+"/"+str(C[i])+"}",end="")
print("}")