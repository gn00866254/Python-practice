# Python - open file(1) - Exercise
## 問1：
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
```python=
file_name = input("Please enter the file name:")
file = open(file_name, 'r')
print(file.read())
file.close()
```

## 問2：
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
```python=
f = open("read.txt")
string = f.read()
sp_str = string.split()

s= 0 #総和を格納する変数
for i in sp_str:
    s+=int(i)　#格納していく
print(s)
f.close()
```

## 問3：
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
```python=
f = open("read.txt")
string = f.read()
sp_str = string.split()
#削除前
print("=== Before the deletion ===")
print(sp_str)
#削除したい
s = input("Please enter the text you want to delete: ")
sp_str.remove(s)
#削除後
print("=== After the deletion ===")
print(sp_str)
f.close()
```

## 問4：
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
