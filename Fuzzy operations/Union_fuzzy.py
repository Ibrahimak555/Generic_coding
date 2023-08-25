A=dict()
B=dict()
C=dict()

A={165:0.0, 175:0.0, 180:0.0, 182.5:0.25, 185:0.5, 190:1.0}
B={165:0.0, 175:1.0, 180:0.0, 182.5:0.5, 185:0.25, 190:0.0}

for i in A:
    C[i] = max(A[i],B[i])

print("{",end='')
c=0
for i in C:
    c = c+1
    if c < len(C):
        print("("+str(C[i])+"/"+str(i)+")",end=",")
    else:
        print("("+str(C[i])+"/"+str(i)+")",end="")
print("}")