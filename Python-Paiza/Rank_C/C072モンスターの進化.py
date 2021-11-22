#print(E)
atk,defe,agi=input().split()
atk,defe,agi=int(atk),int(defe),int(agi)
monster_n=int(input())
count=0
monster=[]
monsterName=[]
for i in range(monster_n):
    monster.append(input().split())

for i in monster:
    count=0
    if atk >= int(i[1]) and atk <= int(i[2]):#攻撃
        count+=1
    if defe >=int(i[3]) and defe <= int(i[4]):#防御
        count+=1
    if agi >= int(i[5]) and agi <= int(i[6]):#素早さ
        count+=1
    if count ==3 :
        monsterName.append(i[0])

if len(monsterName)==0:
    print("no evolution")
else:
    for i in monsterName:
        print(i)
