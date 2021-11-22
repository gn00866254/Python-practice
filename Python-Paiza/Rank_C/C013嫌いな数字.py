hatenum=input() #嫌いな数字
roomnum=int(input())#病室の総数
count=0#合計
allroom=[]
for i in range(roomnum):
    allroom.append(input())

for i in allroom:
    if hatenum in i: #もし嫌な数字がある場合
        pass
    else:
        count+=1
        print(i)
        
if count==0:#もし存在しないなら「none」
    print("none")
