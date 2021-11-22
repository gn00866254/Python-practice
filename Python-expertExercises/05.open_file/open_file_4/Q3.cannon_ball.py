# -*- coding: utf-8 -*-
def readfile(fname):
    file=open(fname)
    #タイトルを取得
    title=file.readline()
    gameNum=len(file.readline().strip().split()[1:])
    #IDをkeyとして、成績を値として格納
    contents=file.readlines()
    return title,contents,gameNum

def getscore(contents):
    id_scoredict={}
    #先取得有幾筆成績，並將它作為index使用
    for index in range(len(contents)):
        line=contents[index].split()
        scores=[int(i) for i in line[1:]] #ID以外的成績
        humanid=line[0] #ID
        #ID為KEY 成績為值
        id_scoredict[humanid]=scores
    return id_scoredict

def getGamescore(contents,gameNum):
    #做一個有每一次射擊成績的字典 Key:第幾比賽 value:那場比賽的成績。
    r_scoredict={}
    for i in range(gameNum):
        scorelist=[]
        for j in range(50):
            line=contents[j].split()#一樣取得每一行
            scores=line[1:] #ID以外取成績
            scorelist.append(int(scores[i]))
            r_scoredict[i+1] = scorelist
    return r_scoredict

#取得指定場的字典
def getsinglescore(r_scoredict,rankNum):
    singledict={}
    for i in range(len(r_scoredict[rankNum])):
        score = r_scoredict[rankNum][i]
        singledict[i+1]=score
    return singledict
        
#將字典的值加總並回傳一個新字典的函數
def sumDict(scoredict):
    sumDict={}
    for key,value in scoredict.items():
        sumDict[key]=sum(value)
    return sumDict

#將加總過後的字典的值做排序後比對，並依照值得大小順序回傳新的字典
def getRank(sumdict):
    sumrank=sorted(sumdict.values(),reverse=True)
    rankdict={}
    for sumNum in sumrank:
        for k,v in sumdict.items():
            if sumNum==v:
                if k in rankdict:
                    continue
                else:
                    rankdict[k]=v
                    break
    return rankdict


fname="cannon.txt"
#讀檔
title,contents,gameNum=readfile(fname)
#每個人成績及每回合成績的DICT
id_scoredict=getscore(contents)
r_scoredict=getGamescore(contents,gameNum)
#取得每一個人的總和
id_sum=sumDict(id_scoredict)
#取得每一回合的總和
r_sum=sumDict(r_scoredict)

while True:
    select_num = int(input("1.個人総合Rank　2.各試射総合Rank　3.各試射個人Rank:"))
    target=0
    item=""
    if select_num == 1:
        target=id_sum
        item="ID"
    elif select_num == 2:
        target=r_sum
        item="Game"
    elif select_num == 3:
        rankNum=int(input("何試合目のRank："))
        target=getsinglescore(r_scoredict,rankNum)
        item="ID"
    rankdict=getRank(target)
    
    #列印排名
    print(title)
    print("-"*24)
    print("|{:<7}|{:^5}|{:>8}|".format("NO.",item,"Score"))
    print("-"*24)
    count=1
    through=1
    prev=0
    for k,v in rankdict.items():
        if v==prev: #如果值和前一個一樣則排名一樣
            print("|No.{:<4}|{:^5}|{:>8}|".format(count-1,k,v))
            print("-"*24)
            through+=1
            continue
        else:
            print("|No.{:<4}|{:^5}|{:>8}|".format(count,k,v))
            count+=through
            through=1
            prev=v
            print("-"*24)
