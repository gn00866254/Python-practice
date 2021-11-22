# coding: utf-8
import math
taxiN,distance=map(int,input().split())

costlist=[]
for i in range(taxiN):
    fdis,fmoney,add_dis,add_money=map(int,input().split())
    if distance <fdis:
        costlist.append(fmoney)
    elif distance==fdis:
        costlist.append(fmoney+add_money)
    else:
        dis=distance-fdis
        if dis%add_dis==0:
            num=dis//add_dis
            cost=fmoney+(num+1)*add_money
            costlist.append(cost)
        else:
            num=math.ceil(dis/add_dis)
            cost=fmoney+num*add_money
            costlist.append(cost)
print("{} {}".format(min(costlist),max(costlist)))
