def create_dict(itemMoney):
    pdut_dict={}
    for i in range(len(itemMoney)):
        pdut_dict[i+1]=itemMoney[i]
    return pdut_dict

#道具の個数
n=int(input())
#価額表を用意
itemMoney=list(map(int,input().split()))
product_dic=create_dict(itemMoney)

#金額と注文回数
myMoney,times = map(int,input().split())

for i in range(times):
    item_no,many=map(int,input().split())
    cost=product_dic[item_no]*many
    if myMoney>=cost:
        myMoney-=cost
    else:
        continue
print(myMoney)
"""
#old_version
#道具の個数
n=int(input())
itemMoney=input().split(" ") 
mym,time = input().split()

mymoney=int(mym)
times=int(time)

log=[]
for i in range(times):
    item,many = input().split()
    log.append([item,many])

for i in range(len(log)):
    if mymoney >= int(itemMoney[int(log[i][0])-1])*int(log[i][1]):
        mymoney -=int(itemMoney[int(log[i][0])-1])*int(log[i][1])
        
    elif mymoney < int(itemMoney[int(log[i][0])-1])*int(log[i][1]):
        continue

print(mymoney)
"""
