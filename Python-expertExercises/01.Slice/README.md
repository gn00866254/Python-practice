# スライス - HomeWork

## 問題1：語尾判断
以下の条件を満たすプログラムを作成してください。
単語の末尾が入力した語尾かどうかを判定します。(スライスを必ず使用します)
* 一つの単語を入力してください
* 判定する語尾を入力してください。
* 単語の末尾が入力の語尾であるかどうかを判別します。そうであればTrueを表示し、そうでない場合はFalseを表示します。
### 出力：
```
please enter string: connection
Please enter the suffix you want to judge: tion
True

please enter string: connection
Please enter the suffix you want to judge: er
False

please enter string: function
Please enter the suffix you want to judge: ct
False

please enter string: function
Please enter the suffix you want to judge: ion
True
```
code:  
[Answer](https://github.com/gn00866254/Python-practice/blob/main/Python-expertExercises/01.Slice/01_suffix_judge.py)

## 問題２：成績判定
次の条件を満たすプログラムを作成してください。
* まず、ユーザーに成績の個数を表すnを入力させます。
* 次に、成績を整数1から100の乱数でn個生成して出力します。
* 最後、より客観的な採点のために、最高点と最低点を取り除き、小さいものから大きいものに並べてください。(スライスを必ず使用します)

### 出力：
```
Input n: 10
Original: [79, 90, 94, 36, 8, 87, 66, 5, 60, 59]
Result: [8, 36, 59, 60, 66, 79, 87, 90]

Input n: 15
Original: [86, 20, 57, 75, 78, 32, 66, 73, 82, 89, 91, 95, 13, 12, 8]
Result: [12, 13, 20, 32, 57, 66, 73, 75, 78, 82, 86, 89, 91]
```

stepが負数の場合
```
>>> seq[::-stride]        # [seq[-1],   seq[-1-stride],   ..., seq[0]    ]
>>> seq[high::-stride]    # [seq[high], seq[high-stride], ..., seq[0]    ]
>>> seq[:low:-stride]     # [seq[-1],   seq[-1-stride],   ..., seq[low+1]]
>>> seq[high:low:-stride] # [seq[high], seq[high-stride], ..., seq[low+1]]
```
code:  
[Answer]()

