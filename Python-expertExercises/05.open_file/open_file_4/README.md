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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_4/Q1.jackpot.py


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
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_4/Q2.write_cannon.py


## 問３：砲弾射撃記録の読み込み
以下の砲弾射撃ファイルを読み込み、必要なデータを抽出しましょう。

[砲弾射撃記録ファイル](https://drive.google.com/file/d/13JCxgUzZ-tIh8OeWjzZVBMQ9jmbkb00m/view?usp=sharing)

code:  
https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/05.open_file/open_file_4/Q3.cannon_ball.py
