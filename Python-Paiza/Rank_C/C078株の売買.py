N,c_1,c_2 = map(int,input().split())
profit=0
stock=0
stockvalue=[int(input()) for i in range(N)]

for i in stockvalue:
    #1株購入
    if  i <= c_1:
       stock+=1
       profit-=int(i)
    #売る
    elif i>= c_2:
        profit+=int(i)*stock
        stock=0
        
    #N 日目には、上記を行わず持ち株をすべて売る
    if (N-1) == stockvalue.index(i):
        profit+=int(i)*stock

print(profit)
