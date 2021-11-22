N = int(input())#文字列の数 N
G = input()#抽出する対象の重要な文字列 G 
log=[input() for i in range(N)]#入力した文字列
count=0
for i in log:
    if G in i:　#存在しているなら出力し、１を足す
        print(i)
        count+=1

if count == 0:
    print("None")
