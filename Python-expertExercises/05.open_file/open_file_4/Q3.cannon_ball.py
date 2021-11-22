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
    #成績データの長さを計り、indexとして使う
    for index in range(len(contents)):
        line=contents[index].split()
        scores=[int(i) for i in line[1:]] #ID以外的成績
        humanid=line[0] #ID
        #ID為KEY 成績為值
        id_scoredict[humanid]=scores
    return id_scoredict

def getGamescore(contents,gameNum):
    #試合ごとの成績を持つ辞書を作成　Key:試合NO value:成績
    r_scoredict={}
    for i in range(gameNum):
        scorelist=[]
        for j in range(50):
            line=contents[j].split()
            scores=line[1:] #ID以外の成績
            scorelist.append(int(scores[i]))
            r_scoredict[i+1] = scorelist
    return r_scoredict

#指定した試合の成績を取得
def getsinglescore(r_scoredict,rankNum):
    singledict={}
    for i in range(len(r_scoredict[rankNum])):
        score = r_scoredict[rankNum][i]
        singledict[i+1]=score
    return singledict
        
#試合成績の合計を計算し、辞書にする。
def sumDict(scoredict):
    sumDict={}
    for key,value in scoredict.items():
        sumDict[key]=sum(value)
    return sumDict

#加算した辞書の値をソートして、新たな辞書を返す。
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
#読込
title,contents,gameNum=readfile(fname)
#皆の成績と試合ごとの成績をもつ辞書の作成
id_scoredict=getscore(contents)
r_scoredict=getGamescore(contents,gameNum)
#皆の成績の合計
id_sum=sumDict(id_scoredict)
#試合ごとの成績の合計
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
    
    #ランクを出力
    print(title)
    print("-"*24)
    print("|{:<7}|{:^5}|{:>8}|".format("NO.",item,"Score"))
    print("-"*24)
    count=1
    through=1
    prev=0
    for k,v in rankdict.items():
        if v==prev: #成績が同じだったら、ランクも一緒。
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
