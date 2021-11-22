# Python 辞書（dict）練習問題 - HomeWork

## 1、価格表
次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| Fatal Frame: Maiden of Black Water     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| Kuon     | 6126     | 
| Corpse Party     | 1520    | 

出力例のようなテーブルを表示してください
### 出力例：
![](https://i.imgur.com/9yXDXnX.png)
```python=
gamedic={"BIOHAZARD Village":9990,
         "Fatal Frame: Maiden of Black Water":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "Kuon":6126,
         "Corpse Party":1520}

print("-"*53)
print("|{:<40}|{:>10}|".format("Game","Price"))

for k,v in gamedic.items():
    print("-"*53)
    print("|{:<40}|{:>10}|".format(k,v))

print("-"*53)
```



## 2、以下の条件を満たすシーザーサラダならぬ「シーザー暗号」の暗号化プログラムを作成してください。
* 平文を入力すること。
* アルファベットをずらす数を入力すること。
* 辞書を出力すること
* 平文と暗号文を出力すること。

**ヒント１**：シーザー暗号とは文字を指定した数だけずらす暗号で、換字式暗号とも言われる簡単な暗号です。例えば、3文字をすらした場合、「a」は「d」に置き換わり「b」は「e」に置き換わります。
![](https://i.imgur.com/Vy20YPh.png)

**ヒント2**：Pythonで暗号化する際に辞書を換字表として利用できます。要は、概念としては平文（暗号化される前の文）をキー（key）にし、暗号文を値にすることで、暗号化を可能にします。

入力例1： 
![](https://i.imgur.com/IUSXLM4.png) 
出力例1： 
![](https://i.imgur.com/0wqc2rr.png) 
入力例2： 
![](https://i.imgur.com/qAntJoS.png) 
出力例2： 
![](https://i.imgur.com/MIM19Qc.png) 

```python=
abcdict={}
abc=list("abcdefghijklmnopqrstuvwxyz")
string=input("暗号化したい文を入力してください：")
num=int(input("何文字をずらすかを入力してください："))

newabc=list(abc[num:]+abc[:num])
for i in range(26):
    abcdict[abc[i]]=newabc[i]
print(abcdict)

print("平文：",string)
print("暗号文：",end="")
for i in string:
    print(abcdict[i],end="")
```

## 3、入力した数字をモールス信号に変換するプログラムを作成してください。
以下はモール信号の一覧です。
1: .----
2: ..---
3: ...--
4: ....-
5: .....
6: -....
7: --...
8: ---..
9: ----.
0:-----

入力例１： 
![](https://i.imgur.com/zqK2A8z.png) 
出力例１： 
![](https://i.imgur.com/WjAySvr.png) 
入力例２： 
![](https://i.imgur.com/G8l3fSK.png) 
出力例２： 
![](https://i.imgur.com/b3j8s7Z.png) 

```python=
dic={1: ".----",
2: "..---",
3: "...--",
4: "....-",
5: ".....",
6: "-....",
7: "--...",
8: "---..",
9: "----.",
0:"-----"}

n_string=input("数字を入力して下さい：")
for ch in n_string:
    code=dic.get(int(ch),"")
    print(code)
```

## 4. カードの合計
1セット13枚のトランプ（2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A）が存在し、2名のプレイヤーがそれぞれ13枚の中からランダムに5枚引く。プレイヤーは自身で引いたトランプにある数値を全て加算(A = 1, J = 11, Q = 12, K = 13)して自身のポイントとし、プレイヤーは互いのポイントの比較を行うこと。最後にはポイントが多い方を勝者として名前を表示して、引き分けであれば「Draw」と表示すること。

### 出力例
```
player 1: ['3', '6', 'A', '4', '7'], Total number: 21
player 2: ['K', '5', 'J', '9', '2'], Total number: 40
Winners: player 2

player 1: ['Q', '6', '2', '10', '8'], Total number: 38
player 2: ['5', 'J', 'K', '3', 'A'], Total number: 33
Winners: player 1
```
```python=
import random
cardDict={1:"A",11:"J",12:"Q",13:"K"}
#ランダムに十枚
cardList=[]
for i in range(10):
    num=random.randint(1,13)
    while num in cardList:
        num=random.randint(1,13)
    cardList.append(num)
#プレイヤー1と2に半分渡す
player1=cardList[:5]
player2=cardList[5:]
#総和を求める
player1_sum=sum(player1)
player2_sum=sum(player2)
#辞書で数値を指定した英文字に変える。
player1_output=[cardDict.get(i,i) for i in player1]
player2_output=[cardDict.get(i,i) for i in player2]
#出力
print("player 1: {}, Total number: {}".format(player1_output,player1_sum))
print("player 2: {}, Total number: {}".format(player2_output,player2_sum))

#総和で勝敗を判定し出力：
if player1_sum==player2_sum:
    print("Draw")
elif player1_sum>player2_sum:
    print("Winners: player 1")
else:
    print("Winners: player 2")
```
