numlist=list(map(int,input().split()))#a, b, c, d はそれぞれ 4 枚のカード
newlist=sorted(numlist)#昇順に並び替え #例： 2, 3, 8 , 9
num1=str(newlist[3])+str(newlist[1])
num2=str(newlist[2])+str(newlist[0])
print(int(num1)+int(num2))
