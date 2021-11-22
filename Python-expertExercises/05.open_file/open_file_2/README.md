# Python - open file(2) - Exercise

## 問1：一行一行
ファイル「game.txt」の内容を読み込み、何行目表示するかを自由に決められるようにするプログラムを作ってください。

```
以下はgame.txtファイルの内容

Game,Price
BIOHAZARD Village,9990
Fatal Frame: Maiden of Black Water,6600
SILENT HILL 3,990
SIREN 2,9800
Kuon,6126
Corpse Party,1520
```
```
**入力１：**
何行目まで出力しますか：2
**出力１：**
Game,Price

BIOHAZARD Village,9990

**入力２：**
何行目まで出力しますか：5
**出力２：**
Game,Price

BIOHAZARD Village,9990

Fatal Frame: Maiden of Black Water,6600

SILENT HILL 3,990

SIREN 2,9800

```

code：
```python=
file=open("game.txt")
num=int(input("何行目まで出力しますか："))
for i in range(num):
    print(file.readline())
file.close()
```

## 問2：一行一行
ファイル「score.txt」の内容を読み込み、総和を求める。
```
以下はscore.txtファイルの内容
80
90
70
55
12
84
00
48
32
84
20
99
end

**出力：**
総和：674
```
code：
```python=
file=open("score.txt")
score=[i for i in file]
newscore=[int(i) for i in score[:-1]]
print("総和：{}".format(sum(newscore)))
```

## 問3：読み込み出力
ファイル「game.txt」の内容を読み込み、出力例のように出力すること。
* gameとpriceの幅はそれぞれ40と10です。
```
以下はgame.txtファイルの内容

Game,Price
BIOHAZARD Village,9990
Fatal Frame: Maiden of Black Water,6600
SILENT HILL 3,990
SIREN 2,9800
Kuon,6126
Corpse Party,1520
```
出力例：
![](https://i.imgur.com/FwmcFzw.png)

code：
```python=
#アクセス
file=open("game.txt")
#幅は40+10、棒三つなので53個「-」
print("-"*53)
#一行ずつ
for lines in file:
    #行ごとにリストにし、出力する。
    line=lines.split(",")
    print("|{:<40}|{:>10}|".format(line[0],line[1].replace("\n","")))
    print("-"*53)
file.close()
```


## 問4：読み込み、ゲーム値段。
ファイル「game.txt」の内容を読み込み、一番高いゲームと一番安いゲームを出力してください。
```
以下はgame.txtファイルの内容

Game,Price
BIOHAZARD Village,9990
Fatal Frame: Maiden of Black Water,6600
SILENT HILL 3,990
SIREN 2,9800
Kuon,6126
Corpse Party,1520
```

出力例：
```
The most expensive is BIOHAZARD Village
The cheapest is SILENT HILL 3
```

code：
```python=
#ファイルアクセス
file=open("game.txt")
#ゲーム値段表
gamedict={}
file.readline() #一行目を読み込み。

for lines in file:
    #行ごとに読み込み、リストの要素をそれぞれの変数に格納。
    line=lines.split(",")
    gameName,price=line[0],int(line[1].replace("\n",""))
    #変数をそれぞれ辞書のキーと値として辞書に追加・
    gamedict[gameName]=price
file.close()

#一番高いのと一番安い
expensive=max(gamedict.values())
cheap=min(gamedict.values())
#もし値が一番高い値段と一致していればキーを出力。反対に、安いときは安いゲームのキーを。
for k,v in gamedict.items():
    if v==expensive:
        print("The most expensive is {}".format(k))
    elif v==cheap:
        print("The cheapest is {}".format(k))
```

## 問5：モンスター
ファイル「monster.txt」の内容を読み込み、指定したモンスターの能力値を確認できるプログラムを作ってください。まず、入力例のように内容を表示し、次にモンスターを指定できるようにします。指定したら指定されたモンスターの能力値と能力の平均値を出力します。なお、平均値を出力の際に、小数点以下二桁で出力してください。

```
以下はmonster.txtファイルの内容
Monster
Name atk def
Alice 80 100
Arsene 150 70
Bobo 99 85

```

```
**入力：**
Name atk def
1.Alice 80 100
2.Arsene 150 70
3.Bobo 99 85

どれが見たい？2

**出力：**
Name:Arsene , Atk: 150 , Def: 70 ,Ave: 110.00

```
code：
```python=
def monTable(contents):
    name,atk,defen=[],[],[]
    for i in contents:
        monData=i.split()
        name.append(monData[0])
        atk.append(monData[1])
        defen.append(monData[2])
    return name,atk,defen

#アクセス
file=open("monster.txt")
file.readline()
title=file.readline()
contents = file.readlines()
file.close()
#タイトルを表示する。
print(title[:-1])
#モンスターを表示する。
num=0
for i in contents:
    print("{}.{}".format(num+1,i[:-1]))
    num+=1

#指定する。
index=int(input("どれが見たい？"))
#文字列を処理して、数値を抽出する。
name,atk,defen = monTable(contents)
#指定したモンスターのデーターを変数に格納。
sName=name[index-1]
sAtk=int(atk[index-1])
sDefen=int(defen[index-1])
sAve=(sAtk+sDefen)/2
#出力する。
print("Name:{} , Atk: {} , Def: {} ,Ave: {:.2f}".format(sName,sAtk,sDefen,sAve))
    
```
