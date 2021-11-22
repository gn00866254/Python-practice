# Python - open file(1) - Exercise
## 問1：会社名ファイルの出力
以下は会社名のテキストファイルです。ユーザーがファイル名を入力し、ファイルの内容を印刷するためのプログラムを作成してください。
Company.txt
```
Craft Egg 
BANDAI 
Cygames
SquareEnix
KONAMI
```

```
**入力例：**
Please enter the file name:Company.txt

**出力例：**
Craft Egg 
BANDAI 
Cygames
SquareEnix
KONAMI
```

code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/Q1.company_name.py

## 問2：ファイルデータの合計
「read.txt」ファイルの内容（内容はスペースで区切られている数字）を読み込み、それらの合計を計算し出力するプログラムを作成せよ。読み込み終了したらファイルを閉じること。
read.txt
```
11 22 33 22 33 44 33 44 55 44 55 66 55 66 77
```
```
**出力例：**
660
```

code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/Q2.num_sum

## 問3：文字列の削除
文字列「s」を入力させ、ファイル「read.txt」の内容を表示する。その後ファイルの内容から、文字列「s」を含む文字を削除すること。
そして指定した文字列を削除したファイル内容の表示。
read.txt
```
Apple Kiwi Banana Tomato Pear Durian
```
```
**入力出力例：**
=== Before the deletion ===
['Apple', 'Kiwi', 'Banana', 'Tomato', 'Pear', 'Durian']

Please enter the text you want to delete: Tomato
=== After the deletion ===
['Apple', 'Kiwi', 'Banana', 'Pear', 'Durian']
```
code：
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/Q3.delete_string

## 問4：文字列の置換
read.txtファイルを読み込み、ユーザに文字列s1と文字列s2を入力させ、ファイル内の文字列s1をs2に置き換え、元のファイルの内容と置換したファイルの内容を出力するプログラムを作成してください。
read.txt
```
watch shoes skirt pen trunks pants
```
```
入出力例：
please enter s1:pen
please enter s2:senakers
=== Before the replacement
watch shoes skirt pen trunks pants
=== After the replacement
watch shoes skirt senakers trunks pants
```

code：
```python=
str_old = input("please enter s1:")
str_new = input("please enter s2:")
file = open("read.txt", "r")
data = file.read()
print("=== Before the replacement")
print(data)
print("=== After the replacement")
data = data.replace(str_old, str_new)
print(data)
```
結果：
![](https://i.imgur.com/8qI9DPu.png)
