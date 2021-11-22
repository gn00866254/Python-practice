N,M = map(int,input().split())
cost=[]
point=0
output=[]
#かかる運賃
for i in range(M):
    cost=int(input())
    if point>=cost:
        point-=cost
    elif N>=cost: #金額が運賃より大きいなら引いてポイントを入れる。
        N-=cost
        point+=cost//10
    print(N,point)


"""
version1:
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,M = input().split()
N=int(N)
M=int(M)
cost=[]
point=0
output=[]
for i in range(M):
    cost.append(int(input()))
for j in cost:
    if point <= j and N>=j:
        N-=j
        point+=(j//10)
        output.append([N,point])
    elif point>= j:
        point-=j
        output.append([N,point])
        
for i,j in output:
    print(i,j)
"""
