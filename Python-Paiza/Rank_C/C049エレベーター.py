N=int(input()) #ログの行数を表す変数 N 
distance=[]
ans=0
d=1 #現在にいる階層を表す
f_d=0
#止まった階を入力してもらい、リストに格納
for i in range(N):
    f=int(input())
    distance.append(f)


for i in distance:
    f_d=abs(d-i)#現在いる階層を移動先の階層で引くことで移動した階層を計算する。
    ans=ans+f_d #変数に足していく
    d=i#移動先を現在の階層にする。
print(ans)
