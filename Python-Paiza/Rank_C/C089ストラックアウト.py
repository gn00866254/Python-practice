
batsu=[]
point=[]
H,W=input().split()
score=0
for i in range(int(H)):
    batsu.append(list(input()))
    
for i in range(int(H)):
    point.append(input().split())

for i in range(len(batsu)):
    tmp=point[i]
    for j in range(int(W)):
       if batsu[i][j]=="o":
           score+=int(tmp[j])
print(score)
