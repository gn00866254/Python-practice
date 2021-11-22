# Python - open file(3) - Exercise(解答)

## 問1：会社ランキング
以下は入社して良かったランキングののテキストファイルです。コードで以下のファイルを書き込んでください。

![](https://i.imgur.com/uK4droD.png)

code：
```python=
file=open("Company.txt","w")
file.write("入社して良かった会社ランキング2019\n\n")
file.write("一位 グーグル合同会社\n")
file.write("二位 株式会社コスモスイニシア\n")
file.write("三位 マッキンゼー＆カンパニー日本支社\n")
file.close()
```

## 問2：終わらない夏、エンドレスファイル
日記を書くプログラムを作りましょう。
入力できるようにし、入力した内容は「diary.txt」ファイルに書き込まれます。なお、"end"が入力されたらプロブラムを終了します。

* 日記のプログラムなので、計5回実行して、毎回違う内容を書き込みます。5回実行したらファイルの内容は以下の通りになります。
![](https://i.imgur.com/xvQnxm6.png)

```
**入出力１：**
|1973年8月3日

|私には、飼っている犬がいます。

|柴犬で、名前は「コロ」。

|ですがコロは、毎日私の手に噛みついてくるのです。

|本当に愛しくて困ったものです。

|end
---おわり---

**入出力２：**

|1973年8月20日

|コロのこと大好きです。

|でも、餌をやっても、懐いてくれません。

|そんなコロが唯一楽しそうにやってくれる遊びは、ボールをころころと転がす遊びです。

|その遊びだけは、私と一緒に遊んでくれます。

|昨日、ころころしました。

|end
---おわり---

**入出力３：**
|1973年8月21日

|今日も、ころころしました。

|end
---おわり---

**入出力４：**

|1973年8月22日

|今日も、ころころしました。

|今日も、ころころしました。

|今日も、ころころしました。

|end
---おわり---

**入出力5：**
|1973年8月23日

|今日も、＆’＆ろしました。

|’（A'F日も、ころ（（％＆ころしました。

|）A&kyoumo korokoしました。

|end
---おわり---
```

code：
```python=
file=open("read.txt","a")
while True:
    content=input("|")
    if content=="end":
        break
    file.write(content+"\n")
file.close()    
print("---おわり---")
```

## 問3：楽しい地獄
:::danger
七つの大罪、人間は生まれながらにして罪を犯すもの。
そこで如何に自分が陥ってしまった罪から目を覚めるか、
どう向き合っていくか.......
:::
デジタル変革時代の到来でサタン様は業務のデジタル化を推進しています。サタン様の指示に従って以下の条件を満たすプログラムを作成してください。

* まず、以下のファイルを書き込んでください。
![](https://i.imgur.com/tWfMuf0.png)
* 次に、以下の指示に沿って出力してください。
1. タイトルを出力すること。
2. 一番罪深い人間を出力すること。
3. 一番罪が浅い人間を出力すること。
4. 人間がよく犯す二つの罪を出力すること。
* 最後、ユーザーに何番目の人を処刑するかを入力させ、指定した人間のデータをファイルから消してください。
```
入出例1：
Seven deadly sins

一番罪深い人間は？ Judy
一番罪が浅い人間は？ Jerry
人間がよく犯す二つの罪は？傲慢 怠惰 
誰を処刑しますか(1~6までの整数を入力してください)；2
Anzu の存在が消された。
```
![](https://i.imgur.com/lOHq4DA.png)
```
入出例2：
Seven deadly sins

一番罪深い人間は？ Judy
一番罪が浅い人間は？ Jerry
人間がよく犯す二つの罪は？傲慢 怠惰 
誰を処刑しますか(1~6までの整数を入力してください)；6
tomo の存在が消された。
```
![](https://i.imgur.com/aVXRm4c.png)

code：
```python=
def readFile(fname):
    names=[]
    sloth=[]
    greed=[]
    pride=[]
    envy=[]
    total=[]
    file=open(fname,"r")
    title=file.readline()
    file.readline()
    for i in file.readlines():
        line=i.split()
        names.append(line[0])
        sloth.append(int(line[2]))
        greed.append(int(line[3]))
        pride.append(int(line[4]))
        envy.append(int(line[5]))
        total.append(int(line[2])+int(line[3])+int(line[4])+int(line[5]))
    return names,sloth,greed,pride,envy,title,total

def writefile(fname,num=""):
    sinone=""
    f=open(fname,"w")
    stringList=["Seven deadly sins\nName	ID		怠惰	強欲	傲慢	嫉妬",
            "\nenor	###4442		82	55	99	41	",
            "\nAnzu	###7771		97 	36	85	35	",
            "\nBmo	###6669		89	66	89	49	",
            "\nJudy	###3997		69	93	85	81	",
            "\nJerry	###2012		11	76	69	19	",
            "\ntomo	$$$7777		65	75	84	84	"]
    if num=="":
        pass
    else:
        sinone=stringList.pop(int(num))    
    for i in stringList:
        f.write(i)
    f.close()
    return sinone
    


fname="sin7.txt"
writefile(fname)
names,sloth,greed,pride,envy,title,total=readFile(fname)
no1Index=total.index(max(total))
last1Index=total.index(min(total))
    
print(title)
print("一番罪深い人間は？",names[no1Index])
print("一番罪が浅い人間は？",names[last1Index])
print("人間がよく犯す二つの罪は？",end="")

sinTotalList=[sum(sloth),sum(greed),sum(pride),sum(envy)]
sinTotalList.sort()
no1no2List=[sinTotalList[-1],sinTotalList[-2]]
for i in no1no2List:
    if i == sum(sloth):
        print("怠惰",end="")
    elif i== sum(greed):
        print("強欲",end="")
    elif i== sum(pride):
        print("傲慢",end="")
    elif i==sum(envy):
        print("嫉妬",end="")
    print(" ",end="")

userInput=input("誰を処刑しますか(1~6までの整数を入力してください)；")
sinone=writefile(fname,userInput)
print(sinone.split()[0],"の存在が消された。")

```
