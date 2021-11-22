# 辞書(Dictionary) - Exercise 1
## 問1：辞書を作成する
辞書（dict）を一つ作成し、作成する際はそれぞれ"end"がキーとして入力されるまで辞書のキーと値を入力する。（キーは"end"を含まず）

```
入力例：
key : Google
value:グーグル
key : Twitter
value:ツイッター
key : Amazon
value:アマゾン
key : end

出力例：
{'Google': 'グーグル', 'Twitter': 'ツイッター', 'Amazon': 'アマゾン'}
```
![](https://i.imgur.com/Kj5yPSa.png)

code：
```python=
mydic={}
keys=""
values=""
while True:
    key = input("key : ")
    if key != "end":
        value = input("value:")
        mydic.setdefault(key,value)
    else:
        break
print(mydic)
```
結果：
![](https://i.imgur.com/NcC9RC4.png)


## 問2：
次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 

商品名から価格を検索するプログラムを作成してください。
見つからない場合は、「No this game」を表示してください。

```

入力例1：
Enter game name: SIREN 2
出力例1：
9800

入力例2：
Enter game name: PSYCHOBREAK
出力例2：
No this game

入力例3：
Enter game name: 九怨
出力例3：
6126
```
![](https://i.imgur.com/1Vax42C.png)

code：
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

gameName = input("Enter game name: ")
price = gamedic.get(gameName, "No this game")
print(price)
```
結果：
![](https://i.imgur.com/ak8kEE8.png)


## 問3：
次の表はゲームの価格表で、価格表を辞書にしてください。

| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 

商品名から価格を検索するプログラムを作成してください。
見つからない場合は、このゲームを辞書に追加して価格を0にしてください。

```
入力例1：
Enter game name: 零 〜濡鴉ノ巫女〜
出力例1：
零 〜濡鴉ノ巫女〜 : 6600

入力例2：
Enter game name: PSYCHOBREAK
出力例2：
{'BIOHAZARD Village': 9990, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, '九怨': 6126, 'コープスパーティー': 1520, 'PSYCHOBREAK': 0}
```
![](https://i.imgur.com/wiCvmgG.png)

code：
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

gameName = input("Enter game name: ")
price = gamedic.setdefault(gameName,0)
if price:
    print("{} : {}".format(gameName,price))
else:
    print(gamedic)
```
結果：
![](https://i.imgur.com/y05o6i0.png)



## 問4：
次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 

次の表はゲームの価格表で、価格表を辞書にしてください。
見つからない場合は、ゲームを辞書に追加してユーザーに価格を決めてもらいます。
```
入力例1：
Enter game name: 九怨
出力例1：
九怨 : 6126

入力例2：
Enter game name: PSYCHOBREAK
Enter price: 4800
出力例2：
{'BIOHAZARD Village': 9990, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, '九怨': 6126, 'コープスパーティー': 1520, 'PSYCHOBREAK': 4800}
```
![](https://i.imgur.com/agrSzUl.png)

code：
```python=
# -*- coding: utf-8 -*-
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

gameName=input("Enter game name: ")
#辞書にあったら対応する値を取得。なければ追加する。
price=gamedic.setdefault(gameName,0)

#もし値段は0じゃないなら、出力・
if price:
    print("{} : {}".format(gameName,price))
#0はFalseになるので、こちらの処理する。
else:
    #値段を入力
    thePrice=input("Enter price: ")
    #指定したkeyに値を与える。
    gamedic[gameName]=thePrice
    #出力。
    print(gamedic)

```
結果：
![](https://i.imgur.com/O7gpd94.png)


## 問5：
次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 
| PSYCHOBREAK    | 4800   |

辞書関連の関数を使用して、ゲームの名前と価格を出力してください。

```
出力例：
Game name: dict_keys(['BIOHAZARD Village', '零 〜濡鴉ノ巫女〜', 'SILENT HILL 3', 'SIREN 2', '九怨', 'PSYCHOBREAK', 'コープスパーティー'])
Game price: dict_values([9990, 6600, 8990, 9800, 6126, 4800, 1520])
```
![](https://i.imgur.com/2YoLLUQ.png)
code：
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

print("Game name:",gamedic.keys())
print("Game price:",gamedic.values())
```
結果：
![](https://i.imgur.com/5RylCBk.png)

## 問6:
次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 
| PSYCHOBREAK    | 4800   | 

ゲームイベント「E3」の開催と伴い、一部のゲームがセールになっています。辞書でゲームの価格を修正でき、「end」が入力されると修正が止まるようなプログラムを作ってください。

```
Original price: {'BIOHAZARD Village': 9990, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, '九怨': 6126, 'PSYCHOBREAK': 4800, 'コープスパーティー': 1520}
入力例：
I want to change the price of the name of the game: BIOHAZARD Village
New price: 7999
I want to change the price of the name of the game: SILENT HILL 3
New price: 4900
出力例：
I want to change the price of the name of the game: end
Price after promotion: {'BIOHAZARD Village': 7999, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 4900, 'SIREN 2': 9800, '九怨': 6126, 'PSYCHOBREAK': 4800, 'コープスパーティー': 1520}
```
![](https://i.imgur.com/9wv34sC.png)
code:
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}
print("Original price:",gamedic)
while True:
    target=input("I want to change the price of the name of the game: ")
    if target=="end":
        print("Price after promotion:",gamedic)
        break
    newPrice=input("New price: ")
    #gamedic[target]=newPrice
    gamedic.update({target:newPrice})
```
結果：
![](https://i.imgur.com/WatEo17.png)

 ## 問7:
 次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 
| PSYCHOBREAK    | 4800   | 

ゲーム売買プログラムを書いてください。ユーザーに買いたいゲームを入力させ、「end」を入力すると、ユーザーの支払金額を表示してください。これらのゲームの在庫が1つしかないと仮定すると、購入したゲームは辞書から削除する必要があり、実行結果は次のようになります。
```
Original price: {'BIOHAZARD Village': 9990, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, '九怨': 6126, 'PSYCHOBREAK': 4800, 'コープスパーティー': 1520}
入力例：
Want to buy the game: 零 〜濡鴉ノ巫女〜
Want to buy the game: 九怨
Want to buy the game: end
出力例：
Title Money: 12726
{'BIOHAZARD Village': 9990, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, 'PSYCHOBREAK': 4800, 'コープスパーティー': 1520}
```
![](https://i.imgur.com/2A5Swls.png)
code:
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

cost = 0
print("Original price:",gamedic)
while True:
    buyItem=input("Want to buy the game: ")
    if buyItem=="end":
        print("Title Money:",cost)
        print(gamedic)
        break
    cost+=gamedic.get(buyItem,0)
    gamedic.pop(buyItem)
```
結果：
![](https://i.imgur.com/Xv4BqJP.png)

## 問8:
 次の表はゲームの価格表で、価格表を辞書にしてください。

| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 
| PSYCHOBREAK    | 4800   | 

入力されたゲームが辞書に載っているかどうかを確認できるプログラムを書いてください。
```
入力例1：
Enter the game you want to query: SILENT HILL 3
出力例1：
The game is in the dictionary

入力例2：
Enter the game you want to query: Dead by Daylight
出力例2：
The game is not in the dictionary
```
![](https://i.imgur.com/ZtcUXeq.png)
code:
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

check = input("Enter the game you want to query:")

if check in gamedic:
    print("The game is in the dictionary")
else:
    print("The game is not in the dictionary")
```
結果：
![](https://i.imgur.com/1zG6zlW.png)

## 問9：
 次の表はゲームの価格表で、価格表を辞書にしてください。
| Game | Price | 
| -------- | -------- | 
| BIOHAZARD Village    | 9990     | 
| 零 〜濡鴉ノ巫女〜     | 6600    | 
| SILENT HILL 3     | 8990    | 
| SIREN 2     | 9800     | 
| 九怨     | 6126     | 
| コープスパーティー     | 1520    | 
| PSYCHOBREAK    | 4800   | 

Priceを小さいものから大きいものに並べるプログラムを書いてください。
```
**入力例１：**
出力例：
Original price: {'BIOHAZARD Village': 9990, '零 〜濡鴉ノ巫女〜': 6600, 'SILENT HILL 3': 8990, 'SIREN 2': 9800, '九怨': 6126, 'PSYCHOBREAK': 4800, 'コープスパーティー': 1520}
Sorted: [1520, 4800, 6126, 6600, 8990, 9800, 9990]
```
![](https://i.imgur.com/HFCvVyj.png)

Code:
```python=
gamedic={"BIOHAZARD Village":9990,
         "零 〜濡鴉ノ巫女〜":6600,
         "SILENT HILL 3":8990,
         "SIREN 2":9800,
         "九怨":6126,
         "コープスパーティー":1520}

print("Original price:",gamedic)
print("Sorted:",sorted(gamedic.values()))
```
結果：
![](https://i.imgur.com/b3dxd6M.png)
