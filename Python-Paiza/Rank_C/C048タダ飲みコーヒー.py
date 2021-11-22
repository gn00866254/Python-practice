x,p=input().split() #コーヒーの価格を示す整数 X と 割引き率を示す整数 P
p=int(p)
x=int(x)

total=0 #
while x>0:
    total+=x
    x=x-x*(p/100)
    x=int(x) #小数点以下全部切り捨て
    
print(total)
