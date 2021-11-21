# 内包表記 - HomeWork
## 問題１：生年月日の判定
生年月日に関するデータは次の通りです。

```
birthday = ["19930911", "20010621", "19801110", "19980507", "20100101"]
```
本データを内包表記を利用して誕生年、月、日をそれぞれ個別のリストに格納し、要素にそれぞれ「年」、「月」、「日」を付け足すこと。

実行した場合の入出力結果が次の通り：
```
Year List: ['1993年', '2001年', '1980年', '1998年', '2010年']
Month List: ['09月', '06月', '11月', '05月', '01月']
Day List: ['11日', '21日', '10日', '07日', '01日']
```
code：
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/02.%E5%86%85%E5%8C%85%E8%A1%A8%E8%A8%98/01_birth_judge.py)

## 問題２：文字の置換（index）
プログラムを作成し、先ずユーザーに一度に複数の単語を入力可能にし、文字列間はスペースで区切ること。次にそれぞれの単語から欲しい英文字の位置を指定できる様にし、もし指定された位置が存在しない場合は再度入力させること。
最後は内包表記を用い指定された文字だけのリストを生成すること。

実行した場合の入出力結果が次の通り：
```
input string:python algorithm java android google
Select a character in the python: 0
Select a character in the algorithm: 9
Enter again: 2
Select a character in the java: -1
Enter again: 1
Select a character in the android: 5
Select a character in the google: 3
Selected character index: [0, 2, 1, 5, 3]
Selected character elements: ['p', 'g', 'a', 'i', 'g']
```
code：
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/02.%E5%86%85%E5%8C%85%E8%A1%A8%E8%A8%98/02_string_select.py)

## 問題3： 内包表記の判定　if - else
生年月日に関するデータは次の通りです。
```
birthday = ["19930911", "20010621", "19801110", "19980507", "20100101", "20090519", "20140712", "20110323", "19990415", "20001224"]
```
生年月日のデータを用いて計算を行い、その結果を表示すること。
* 生まれが2000年以降の年を表示
* 上記生まれ年の内、その生まれ月が「1～6」又は「7～12」であるかの表示
```
['2001', '2010', '2009', '2014', '2011', '2000']
['7~12', '1~6', '7~12', '1~6', '1~6', '1~6', '7~12', '1~6', '1~6', '7~12']
```
code：
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/02.%E5%86%85%E5%8C%85%E8%A1%A8%E8%A8%98/03_comprehensions_ifelse.py)


## 問題４：内包表記とスライス
以下のWords格納されている単語をプログラムで文字列処理を行い、出力例のように出力してください。

* 末尾がtionとなっている単語の末尾をsに書き換え、新たなリストに追加すること。

```
Words：
['aaation', 'bbbtion', 'ccbtionshh', 'bbs', 'jjtion']

出力例：
['aaas', 'bbbs', 'jjs']
```
code：
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/02.%E5%86%85%E5%8C%85%E8%A1%A8%E8%A8%98/04_comprehensions%26slice.py)
