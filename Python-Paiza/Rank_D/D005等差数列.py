m,n = input().split()

M = int(m)
N = int(n)
listans=[]
for i in range(10):
    listans.append(M)
    M+=N

ans=" ".join(map(str,listans))
print(ans)
