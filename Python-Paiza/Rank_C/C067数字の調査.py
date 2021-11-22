n,x=map(int,input().split())
#100 90
string=bin(x)[2:]#二進数にし、文字列に対しスライスする。
for i in range(n):
    index=int(input())
    print(string[-index])#index指定で文字列の文字を出力
