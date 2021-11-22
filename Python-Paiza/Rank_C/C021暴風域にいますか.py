#2点間の距離の公式で距離を求める
xc,yc,r_1,r_2 = input().split()#中心の座標と半径１と２を入力する。
xc,yc,r_1,r_2=int(xc),int(yc),int(r_1),int(r_2)#intにする

n=int(input())#何個座標を入力する。

result=[]

for i in range(n):
    x,y = map(int,input().split())
    if r_1**2 <= (((x-xc)**2) + ((y-yc)**2)) <= r_2**2:
        print("yes")
    else:
        print("no")
