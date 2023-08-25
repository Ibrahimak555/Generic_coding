A=dict()
A_c=dict()

A={10:0.0, 20:0.3, 30:1.0, 40:0.2, 50:0.5, 60:0.2}

for i in A:
    A_c[i] = 1-A[i]

print("A' = {",end='')
c=0
for i in A_c:
    c = c+1
    if c < len(A_c):
        print("("+str(i)+"/"+str(A_c[i])+")",end=", ")
    else:
        print("("+str(i)+"/"+str(A_c[i])+")",end="")
print("}")