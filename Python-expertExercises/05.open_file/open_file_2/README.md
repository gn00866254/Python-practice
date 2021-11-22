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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_2/Q1.one_line.py

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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_2/Q2.one_line_sum.py

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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_2/Q3.prt_data.py


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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_2/Q4.price.py

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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_2/Q5.monster.py
