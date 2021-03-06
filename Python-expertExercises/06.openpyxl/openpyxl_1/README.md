# Python - Openpyxl（1） - Exercise(解答)

以下の「Sales.xlsx」ファイルを用意しましょう。
![](https://i.imgur.com/KFd8tcQ.png)

## 問題1：セルの取得
「Sales.xlsx」ファイルを読み込み、以下の条件に満たすプログラムを作成せよ

* まず、ファイルを読み込んだら、既存のシートオブジェクトを出力すること。
* 次に、どのシートを操作するかを、選択できるようにすること。
* シートを選択したら、取得したシートオブジェクトを出力すること。
* 最後は、以下三つセルのオブジェクトを取得する機能を選択できるようにし、選択すると選択肢に応じて機能します。
    * 「一つのセルの取得」
    * 「複数のセルの取得」
    * 「指定した行のセルの取得」

```
入力出力例１：

--読込完了--
[<Worksheet "Sheet1">, <Worksheet "Sheet2">, <Worksheet "Sheet3">]

which sheet 1~3:1
Got sheet: <Worksheet "Sheet1">
0:Get one cell , 1: Get multiple cells , 2: Specify a row

Enter:0

Which the cell you want to get:B5
<Cell 'Sheet1'.B5>

入力出力例２：

--読込完了--
[<Worksheet "Sheet1">, <Worksheet "Sheet2">, <Worksheet "Sheet3">]

which sheet 1~3:1
Got sheet: <Worksheet "Sheet1">
0:Get one cell , 1: Get multiple cells , 2: Specify a row

Enter:1

Enter the range:A1:C10
((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>), (<Cell 'Sheet1'.A4>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.C4>), (<Cell 'Sheet1'.A5>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.C5>), (<Cell 'Sheet1'.A6>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.C6>), (<Cell 'Sheet1'.A7>, <Cell 'Sheet1'.B7>, <Cell 'Sheet1'.C7>), (<Cell 'Sheet1'.A8>, <Cell 'Sheet1'.B8>, <Cell 'Sheet1'.C8>), (<Cell 'Sheet1'.A9>, <Cell 'Sheet1'.B9>, <Cell 'Sheet1'.C9>), (<Cell 'Sheet1'.A10>, <Cell 'Sheet1'.B10>, <Cell 'Sheet1'.C10>))

入力出力例３：

--読込完了--
[<Worksheet "Sheet1">, <Worksheet "Sheet2">, <Worksheet "Sheet3">]

which sheet 1~3:1
Got sheet: <Worksheet "Sheet1">
0:Get one cell , 1: Get multiple cells , 2: Specify a row

Enter:2

Enter row:10
(<Cell 'Sheet1'.A10>, <Cell 'Sheet1'.B10>)

```

code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/06.openpyxl/openpyxl_1/Q1.get_cell.py
## 問題2：修正

「Sale.xlsx」ファイルを読み込み、A2~B2のセルを取得し、以下の条件を満たすプログラムを作成せよ

* A2～B2のアドレスと値を出力すること。
* 修正する箇所を入力できるようにすること。
* 値を入力したら、修正後のセルのアドレスと値を出力すること。

```
入出力１：

売上：
A2:Sam、B2:3000
A3:Brian、B3:5000
A4:George、B4:7000

修正する箇所：A3

値：Apple
---修正後：---
売上：
A2:Sam、B2:3000
A3:Apple、B3:5000
A4:George、B4:7000

入出力２：

売上：
A2:Sam、B2:3000
A3:Brian、B3:5000
A4:George、B4:7000

修正する箇所：B2

値：789456123
---修正後：---
売上：
A2:Sam、B2:789456123
A3:Brian、B3:5000
A4:George、B4:7000
```

code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/06.openpyxl/openpyxl_1/Q2.fixed.py

## 問題3：総和
「Sales.xlsx」ファイルを読み込み、A5に総和を、B5にB2～B4の合計を求める書式を書き込んでください。

名前「"Sales_sum.xlsx"」を付けて保存。

**入出力例１：**
![](https://i.imgur.com/ifI4UV2.png)

code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/06.openpyxl/openpyxl_1/Q3.sum
