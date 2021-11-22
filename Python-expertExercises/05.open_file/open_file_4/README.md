# Python - 多国語&&総合練習 - Exercise(解答)

## 問1：Jackpotゲーム
多国語に対応する数字を当てるゲーム「Jackpot」を作りましょう。

このゲームを海外と日本で販売したいので、言語ファイルを読み込み、最初は言語を選択できるようにしてください。そして、もちろんなんですが、英語だったら英語で、日本語だったら日本語で表示してください。

**遊び方：**
言語選択が終わったら、まず数値の範囲を設定できるようにしましょう。範囲の設定を終わらせたら、今度は設定した範囲からランダムに一つの数値をJackpotとして指定しましょう！そして、数値の範囲もJackpotも設定したら、ちゃんと準備ができたってプレイヤーに教えてください。

続いて、当てる回数も設定します。設定し終わったら、ゲーム開始のメッセージを表示し、ゲームスタートです。

ここで注意してほしいのは、ゲームは当てる回数だけ数値を入力できるようにしてください。また、入力した数字により、数字の範囲が変わるので気をつけてください。

もちろん、入力した数値が範囲を超えたとき、当たった時のメッセージと、指定した回数分試しても当たらない時のメッセージも必要なので忘れないでね！

```
以下はjackpot_language.txtファイルの内容

English,日本語
Start from:,開始値:
Ending at:,終了値:
The jackpot and number range settings are complete.,ジャックポットと数字範囲の設定が完了しました。
Count:,回数:
Game START,ゲーム開始
Choise a number from {} to {},{}~{}の数字から一つ選んでください
I told you enter a number from {} to {}!!,{}~{}の数字から一つ選んでって言ったでしょう！
Jackpot is {}.,ジャックポットは{}です！
You win!!,あなたの勝ちです!!
You lost...,あなたの負けです...
```
```
**入出力１：**
1.English 2.日本語 
Which one?1

Start from:1

Ending at:50
The jackpot and number range settings are complete.

Count:5
「-----Game START-----」
Choise a number from 1 to 50

1：25
--------------------------
Choise a number from 25 to 50

2：37
--------------------------
Choise a number from 37 to 50

3：43
--------------------------
Choise a number from 43 to 50

4：45
--------------------------
Choise a number from 45 to 50

5：48
--------------------------
You lost...
Jackpot is 46.

**入出力２：**

1.English 2.日本語 
Which one?2

開始値:1

終了値:30
ジャックポットと数字範囲の設定が完了しました。

回数:5
「-----ゲーム開始-----」
1~30の数字から一つ選んでください

1：15
--------------------------
1~15の数字から一つ選んでください

2：7
--------------------------
7~15の数字から一つ選んでください

3：12
--------------------------
12~15の数字から一つ選んでください

4：14
--------------------------
12~14の数字から一つ選んでください

5：13
ジャックポットは13です！あなたの勝ちです!!

```
code：
#変数に入れる方法１
```python=
import random
#読込
filename="jackpot_language.txt"
file=open(filename)
langList=file.readline().strip().split(",")
#['English', '日本語']言語の選択肢
for i in range(len(langList)):
    print("{}.{}".format(i+1,langList[i]),end=" ")
choiceLang=int(input("Which one?"))

#内容の改行文字を消して、区切り文字で分割してから選んだ言語に対応する内容をリストに格納。
detail=[ i.strip().split(",")[choiceLang-1] for i in file]
#内容をそれぞれの変数に格納。
starText=detail[0]
endText=detail[1]
copletMessa=detail[2]
countText=detail[3]
gameStart=detail[4]
playText=detail[5]
overText=detail[6]
jackpotText=detail[7]
winText=detail[8]
lostText=detail[9]
file.close()

start=int(input(starText))
end=int(input(endText))
jackpot = random.randint(start,end)
print(copletMessa)

count = int(input(countText))
print("「-----"+gameStart+"-----」")
for c in range(count):
    print(playText.format(start,end))
    guess=int(input(str(c+1)+"："))
    if guess<start or guess>end:
        print(overText.format(start,end))
    elif guess == jackpot:
        print(jackpotText.format(jackpot)+winText)
        break
    #もし入力した数字がjackpotより大きい場合、
    #入力した数字を新たなendにする。
    #反対に小さい場合は、startにする。
    elif guess>jackpot:
        end=guess
    elif guess<jackpot:
        start=guess
    print("--------------------------")
#全部試して当たらなかったらmessageを出力する。
else:
    print(lostText)
    print(jackpotText.format(jackpot))
```


## 問２：砲弾射撃記録の作成（ファイル書き込みの練習）
以下はとある砲弾射撃の記録です。
射撃に参加した人数は全部で50人でそれぞれIDがあり、全員100回試射しました。

以下の条件従ってファイルを作成してください。
* 一行目に「砲弾射撃記録」を書き込むこと。
* 二行目に「ID」、「1回目」、「2回目」、、、「100回目」を書き込むこと。
* 三行目以降、ID　と　1回目から100回目までの成績を書き込むこと。
尚、今回は書き込むの練習ということで、成績は全部50～100から一つ乱数を生成し、成績しにてください。
図1：  
![](https://i.imgur.com/Rvtgnve.png)  
図2：  
![](https://i.imgur.com/wpnUHI4.png)  

code：
```python=
import random
def writefile(fname):
    string=""
    f=open(fname,"w")
    #タイトルを書き込み
    title="砲弾射撃記録"
    f.write(title+"\n")
    #一回目から百回目の文字列を用意
    for i in range(100):
        string+="{}回目\t".format(i+1)
    f.write("ID\t"+string+"\n")
    #データを作成する
    for i in range(50):
        content=""
        for j in range(100):
            r_num = random.randint(50,100)
            content +=str(r_num)+"\t"
        f.write("{}\t{}\n".format(i+1,content))
    f.close()

fname="cannon.txt"
#寫檔
writefile(fname)
```


## 問３：砲弾射撃記録の読み込み
以下の砲弾射撃ファイルを読み込み、必要なデータを抽出しましょう。

[砲弾射撃記録ファイル](https://drive.google.com/file/d/13JCxgUzZ-tIh8OeWjzZVBMQ9jmbkb00m/view?usp=sharing)

已可取得1-100場所有人成績，每場比賽每個人的成績，指定場次的所有人成績，

```python=
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
```
