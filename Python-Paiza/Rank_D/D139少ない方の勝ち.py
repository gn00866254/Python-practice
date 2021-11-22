N=input()
N=int(N)
result=[]
result=input().split()
G=0
P=0
for i in result:
    if i == 'G':
        G=G+1
    else:
        P=P+1

if G<P:
    print("G")
elif P<G:
    print("P")
else:
    print("Draw")
