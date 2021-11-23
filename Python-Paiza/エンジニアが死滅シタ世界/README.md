# PAIZA死滅した世界

## 隔離された街のゲート [MISSION LEVEL: B]
```python=
def moveto(d,position):
    #もし入力した文字がU、リスト[x,y]内のyを+1する。
    if d=="U":
        position[1]+=1
    #もし入力した文字がD、リスト[x,y]内のyを-1する。
    elif d=="D":
        position[1]-=1
    #もし入力した文字がL、リスト[x,y]内のxを-1する。
    elif d=="L":
        position[0]-=1
    #もし入力した文字がL、リスト[x,y]内のxを+1する。
    elif d=="R":
        position[0]+=1
    #移動した結果、要はxとy軸を変更した結果をリターンする。
    return position

def check(position):
    """
    マップ内であるか判断するには、いくつの条件がある。
    一つはx,y軸がどれも0以上であること、もう一つはどれもH,Wを超えていないこと。
    要は、以上の条件が成立しなかったら「invalid」、そうでなければ、「valid」。
    """
    if position[0]>int(W)-1 or position[1]>int(H)-1 or position[0]<0 or position[1]<0:
        print("invalid")
    else:
        print("valid")

#マップの縦方向のマス数を表す整数 H 
#横方向のマス数を表す整数 W 
#移動操作の回数を表す整数 N をスペース区切りで入力する。
H,W,N = input().split()
#出発点を表す座標をリストに格納する。
position=[0,0]
#N回移動ということでforループで実行していく。
for i in range(int(N)):
    #実行するたびに、移動の方向を表す文字を入力する。
    d=input()
    #入力した文字を引数として入れ、関数で判断をする。
    position=moveto(d,position)
#最後、終着点を引数として関数に入れ、マップ内であるかどうかを判断する。
check(position)
```


## 高層タワー [MISSION LEVEL: B]　文字列を重ねる
```python=
#word_1の後ろの文字列はtmpと一致するかを判断する関数。　
def endmatch(word_1,tmp):
    #この後、一致するかを判断するための変数。
    match=0
    #indexが範囲を超えないように、まず二つの単語から短い方の長さを取得する。
    minlen=min(len(word_1),len(tmp))

    #ループを使い、index操作で比較する。
    for i in range(minlen):
        #まず、判断する単語が元の単語より大きい場合はそのままループから抜ける
        if len(tmp) > len(word_1):
            break
        #でなければ、判断を行う。　一致であればmatchを一を足す。
        elif tmp[i]==word_1[i-len(tmp)]:
            match+=1
            
    #最後にmatchの長さがtmpと一緒だったら一致でTrue、でなければFalse。
    if match==len(tmp):
        return True
    else:
        return False

                       
def verysuperstrip(word_1,word_2):
    #この後文字列が重ねているかを判断に使う変数を宣言する。
    tmp=""
    #原の単語をここに入れる。
    new_result=word_1
    #そして、ループで重複しているかを判断する。
    for i in word_2:
        #ループが毎回実行されていくたびに、判断する文字列をどんどん追加していく。
        tmp+=i
        #自作のendmatch関数を使い、文字列の後ろはtmpなのかを判断する。
        if endmatch(word_1,tmp):
        #一致しているのならnew_resultを空にする。
            new_result=""
            #一致していないものをnew_resultに入れる。
            for i in range(len(word_1)-len(tmp)):
                new_result+=word_1[i]        
    return new_result+word_2

#結合する単語の個数Nを入力する。
N=int(input())
#単語１の変数を宣言する。
word_1=""
#forのループを使い、N回入力する。
for i in range(N):
    #単語を入力する。
    word_2=input()
    #結果の変数と入力した単語を引数に入れる。
    word_1=verysuperstrip(word_1,word_2)
print(word_1)

"""
def verysuperstrip(word_1,word_2):
    #この後文字列が重ねているかを判断するための変数を宣言する。
    tmp=""
    #本来の結果が変わらないように、新しい結果の変数を宣言する。
    new_result=word_1
    #そして、ループで重複しているかを判断する。
    for i in word_2:
        #ループが毎回実行されていくたびに、判断する文字列をどんどん追加していく。
        tmp+=i
        #自作のendmatch関数を使い、文字列の後ろはtmpなのかを判断する。
        if new_result.endswith(tmp):
            new_result=word_1[:-len(tmp)]
    return new_result+word_2

#結合する単語の個数Nを入力する。
N=int(input())
#結果の変数を宣言する。
word_1=""
#forのループを使い、N回入力する。
for i in range(N):
    #単語を入力する。
    word_2=input()
    #結果の変数と入力した単語を引数に入れる。
    word_1=verysuperstrip(word_1,word_2)
print(word_1)
"""
```
## 砂漠の公園 [MISSION LEVEL: B]　大会の点数

```python=
def getbest(team_info):
    #[チーム番号,スコア,勝った回数,引き分けの回数,負けた回数]のデータが必要なので用意する。
    #チーム番号
    teamnum=team_info[0]
    #勝敗記録の-を消去して、infoの変数に入れる。
    info=team_info[1].replace("-","")
    #スコア
    score=0
    #勝った回数
    win=0
    #引き分けの回数
    draw=0
    #負けた回数
    lost=0
    #ループでinfoから文字を取り出して、判断をする。
    for i in info:
        #Wだったらスコア+2で勝った回数+1
        if i == "W":
            score+=2
            win+=1
        #Dだったらスコア+1で引き分けの回数+1
        elif i=="D":
            score+=1
            draw+=1
        #Lだったらスコア変化なしで負けた回数+1
        elif i == "L":
            lost+=1
    #一通り終わったら、チームの結果をリストで返す。
    teamresult=[teamnum,score,win,draw,lost]
    return teamresult

#優勝チームのスコアと情報を入れる変数とリストを宣言する。
bestscore=0
bestteam=[]
#大会参加人数を表す整数Nを入力する。
N=int(input())
#ループでN回入力する。
for i in range(N):
    #team_infoというリストに[チームの番号、勝敗記録]を格納する。
    team_info=[i+1,input()]
    #そして、自家製のgetbest関数に入れ、返ってきたチームの結果を受け取る。
    teamresult=getbest(team_info)
    #もしスコアがbestscoreより高かったら、スコアをbestscoreにする。
    if teamresult[1]>bestscore:
        bestscore=teamresult[1]
        #そして、そのチーム結果をbestteamにする。
        bestteam=teamresult
#最後は単純に[チーム番号,スコア,勝った回数,引き分けの回数,負けた回数]という風に表示する。
print("{0} {1} {2} {3} {4}".format(bestteam[0],bestteam[1],bestteam[2],bestteam[3],bestteam[4]))

"""
辞書
#優勝チームを獲得する。
def getbest(team_dic):
    #優勝チームのスコア。最初はゼロにする。
    bestscore=0
    #team_dicから各チームのデータを出す。ここで辞書のkeyが順番にiに代入する。
    for i in team_dic:
        #毎回チームごとにスコア計算するのでscoreの変数を宣言する。
        score=0
        #keyを格納したiを利用して、team_dicから各チームの結果を取り出す。
        for j in team_dic[i]:
            #取り出した結果をさらにループを利用して、一つずつ得点のルールに入れ、返ってきた値でscoreを計算する。
            score+=scoredic[j]
        #もしscoreがbestscoreより大きい場合、そのscoreをbestscoreに代入させる。
        if score>bestscore:
            bestscore=score
            #同時にbestteamというLISTに[優勝チーム番号、スコア、勝った回数、引き分けの回数、負けた回数]に格納。
            #ループごとに更新させる。
            bestteam=[i,bestscore,team_dic[i].count("W"),team_dic[i].count("D"),team_dic[i].count("L")]
    return bestteam

#得点のルールの辞書を作る。
scoredic={"W":2,"D":1,"L":0,"-":0}
#大会参加人数を表す整数Nを入力する。
N=int(input())
#各チームの勝敗結果を格納する辞書を作成する。
team_dic={}
for i in range(N):
    #ループを利用して各チームを「何番目のチーム:結果」の形で入れる。
    team_dic[i+1]=input()

#返ってきたbestteamLISTをmapを使い、要素をすべてstrにする。
bestteam=list(map(str, getbest(team_dic)))
#最後にjoinを駆使してスペース区切りでprintする。
print(" ".join(bestteam))
"""
```

## 荒れ果てたショップ [MISSION LEVEL: C]　ゼロを埋める

```python=
#番号の長さを表す整数Nと表示したい番号の区間を表す整数A、Bを入力。
N,A,B=input().split()
#全部intにする。
N=int(N)
A=int(A)
B=int(B)
#forループでそれぞれの数値を出力する。
for i in range(A,B+1):
    #format関数を使い、出力する。
    print("{0:0>{1}}".format(i,N))

"""
N,A,B=map(int,input().split())
for i in range(A,B+1):
    print("{0:0>{1}}".format(i,N))
"""
```
## 学べない学校 [MISSION LEVEL: C]　ジャンケン

```python=

def judge(times):
    #勝利した回数を表す変数を宣言。
    w_a=0
    w_b=0
    #ループで回数Nを実行する。
    for i in range(times):
        #出した手を示す文字を入れる。
        a,b=input().split()
        #aが勝つ可能性を全部並べて、成立したらw_a+1
        if (a=="g" and b=="c") or (a=="c" and b=="p") or (a=="p" and b=="g"):
            w_a+=1
        #bが勝つ可能性を全部並べて、成立したらw_b+1
        elif (b=="g" and a=="c") or (b=="c" and a=="p") or (b=="p" and a=="g"):
            w_b+=1
    #結果をリターンする。
    return w_a,w_b

#じゃんけんする回数Nを入力する。
N=int(input())
#自家製関数judgeに入れる。勝利した回数が返ってくる。
w_a,w_b=judge(N)
print("{0}\n{1}".format(w_a,w_b))
```
**Python**
```python=
n = int(input())
a_win, b_win = 0, 0

win_hand = {"p":"g", "g":"c", "c":"p"} # xが勝つ xが出す手:yが出す手 

for i in range(n):
    a, b = input().split()
    if a == b:#あいこ
        continue

    if win_hand[a] == b:#aの勝ち
        a_win += 1
        
    if win_hand[b] == a:#bの勝ち
        b_win += 1

print(a_win)
print(b_win)
```

## 機械の総合病院 [MISSION LEVEL: C]　文字列判断

```python=
"""
同じ文字が三つ以上連続で使用されているかを判断する関数。
そうあれば、Trueを返す。
そうでなければ、何も返さないので結果的にNoneを返す。
"""
def checktriple(password):
    #今回はパスワードの一番目を後ろの二番と三番と比較し、同じであるかどうかを判断する。
    #従って、パスワードの長さを-2
    for i in range(0,len(password)-2):
        #判断に使うcount。
        count=0
        #index「i」の要素をindex「i+1」,「i+2」と比較する。
        for j in range(i+1,i+3):
            #同じものだったらcount+1する。
            if password[i] == password[j]:
                count+=1
                #もし2だったら「i」「i+1」「i+2」が同じということで、Trueをリターンする。
                if count ==2:
                    return True

#英数字を含んでいるかを判断する関数
def alpha_num(password):
    def checktriple(password):
    for i in range(0,len(password)-2):
        #計算每個字的後三碼是否一樣。 是的話回傳true
        if password[i:i+3].count(password[i])==3:
            return True
            
def alpha_num(password):
　　#数字ありと英文字ありの変数を作り、それぞれFalseにする。
    havenum=False
    havealp=False
    #ループでパスワードを調べる。
    for i in password:
        #数字だったらhavenumをTrue
        if i.isalnum():
            havenum=True
        #文字だったらhavealpをTrue
        if i.isalpha():
            havealp=True
    #両方とも必要なのでandでリターンする。
    return havenum and havealp
    
t=input()
if len(t)>=6 and alpha_num(t) and not checktriple(t):
    print("Valid")
else:
    print("Invalid")

#チェックする文字列を入れる。
t=input()
#もし６以上で英数字を含み、同じ文字が三つ以上連続使用されていなければ、Valid。
#そうでなければ、Invalid。
if len(t)>=6 and alpha_num(t) and not checktriple(t):
    print("Valid")
else:
    print("Invalid")
    
    
"""
def checktriple(password):
    for i in range(0,len(password)-2):
        #文字列の範囲を決め、iからi+2までの間からiがいくつあるかを調べる。
        #3だったらTrueをリターンする。
        if password[i:i+3].count(password[i])==3:
            return True

def alpha_num(password):
    #パスワードをすべて調べ、判断したboolをリストに入れて、最終的にTrueが入ってるかで判断をしてリターンする。
    num=[i.isdigit() for i in password]
    alpha=[i.isalpha() for i in password]
    return True in num and True in alpha

t=input()
if len(t)>=6 and alpha_num(t) and not checktriple(t):
    print("Valid")
else:
    print("Invalid")
"""
```

## 隔離された街のゲート [MISSION LEVEL: B]

```python=
# coding: utf-8
def moveto(d,position):
    if d=="U":
        position[1]+=1
    elif d=="D":
        position[1]-=1
    elif d=="L":
        position[0]-=1
    elif d=="R":
        position[0]+=1
    return position

def check(position):
    if position[0]>int(W)-1 or position[1]>int(H)-1 or position[0]<0 or position[1]<0:
        print("invalid")
    else:
        print("valid")



H,W,N = input().split()
position=[0,0]
for i in range(int(N)):
    d=input()
    position=moveto(d,position)
check(position)
```
