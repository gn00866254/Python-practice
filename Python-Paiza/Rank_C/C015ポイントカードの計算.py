import math
N=int(input()) ##各レシートの数
point=0
for i in range(N):
    d_1,p_1 = input().split()　##1枚目のレシートの日付と購入金額。
    p_1=int(p_1)#金額をintにする。
    if "3" in d_1:#３がつく日だったら購入金額の 3 ％（小数点以下切り捨て）とする
        point+=math.floor(p_1*0.03)
    elif "5" in d_1:#5 のつく日は購入金額の 5 ％（小数点以下切り捨て）とする
        point+=math.floor(p_1*0.05)
    else:
        point+=math.floor(p_1*0.01)
print(point)
