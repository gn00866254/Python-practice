def check(a,b,x,y,r):
  #距離を計算する距離
    if (x-a)**2+(y-b)**2 >= r**2:
        return True 
    else:
        False

#工事現場のx座標,工事現場のy座標,工事現場の騒音の大きさ
a,b,R =map(int,input().split())
point=int(input())#木陰の数
for i in range(point):
    x,y=map(int,input().split())#木陰のx座標,木陰のy座標
    if check(a,b,x,y,R):
        print("silent")
    else:
        print("noisy")
