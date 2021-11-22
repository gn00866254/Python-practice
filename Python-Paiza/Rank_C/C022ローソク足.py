n=int(input())#何日なのか
#0始値、1終値、2高値、3安値
stock=[]
for i in range(n):
    stock.append(input().split())

start = stock[0][0]
end = stock[-1][1]

maxN=0
minN=int(stock[0][3])
#stockからデータを取り出し、比較することで最大値と最小値を取得
for i in stock:
    if maxN < int(i[2]):
        maxN = int(i[2])
        
    if minN > int(i[3]):
        minN = int(i[3])
print(start,end,maxN,minN)
