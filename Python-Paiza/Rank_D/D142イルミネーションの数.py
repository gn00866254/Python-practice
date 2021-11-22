N,X,Y = map(int,input().split())
count=1
tree=1
while tree<=N:
    temp=tree+X
    if temp>N:
        break
    tree=temp
    count+=1
print(count*Y)
