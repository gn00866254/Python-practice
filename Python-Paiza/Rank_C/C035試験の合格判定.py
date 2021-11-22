count=0#通過人数
people=int(input())
for i in range(people):
  #入力されるのは、文理、英語、数学、理科、国語、地理歴史。
    scorelist=input().split()
    subject=scorelist.pop(0)#文理を区別する文字をpopします。
    scorelist=list(map(int,scorelist))#intにします。
    if sum(scorelist)>=350:
        if subject=="s":
            if scorelist[1]+scorelist[2]>=160:
                count+=1
        elif subject=="l":
            if scorelist[3]+scorelist[4]>=160:
                count+=1
print(count)
