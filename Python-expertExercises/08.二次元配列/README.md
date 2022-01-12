# 二次元配列 - HomeWork(解答)
###### tags: `Python HomeWork`

## １、💣と🥔　ばくだんとじゃがいも
💣を掘るゲームを作りましょう！

* 🥔菜園の高さ**h**と幅**w**を入力し、菜園を出力すること。
例えば：3 3を入力する。
![](https://i.imgur.com/L0Eq8mK.png)

* 次に、💣を生成する個数を入力して、ランダムに生成すること。
例えば：2を入力したら、(2,1)と(0,2)が💣とする。

* 最後に、💣を全部掘り出すまで、xとyを入力すること。
xとyを入力して、もし💣だったら💣を表示します。
🥔だったら🥔を表示します。
:::info
入力された値はすべて範囲内とします。
また、重複しないとします。
:::
![](https://i.imgur.com/snkOPj1.png)

実行例１：
![](https://i.imgur.com/26gVD6T.gif)

実行例２：
![](https://i.imgur.com/6MJjsZl.gif)

code:
```python=
import random
def make_map(h,w):
    map_list=[]
    for i in range(h):
        col=[]
        for j in range(w):
            col.append("🔘")
        map_list.append(col)
    return map_list

def prt_map(game_map):
    for row in game_map:
        for col in row:
            print(col,end=" ")
        print()

def create_boom(boom_num)->set:
    boom_set=set()
    while len(boom_set)<boom_num:
        x=random.randint(0,w-1)
        y=random.randint(0,h-1)
        boom_set.add((x,y))
    return boom_set
    

#Input size of map and boom_number
user_input=input("h * w :").split()
h=int(user_input[0])
w=int(user_input[1])
boom_num=int(input("How many boom?"))

#make and print game map
map_list=make_map(h,w)
prt_map(map_list)
#create boom
boom_loc=create_boom(boom_num)

life=0
while life!=boom_num:
    loc=input("x and y:").split()
    x=int(loc[0])
    y=int(loc[1])
    selected=(x,y)
    if selected in boom_loc:
        life+=1
        map_list[y][x]="💣"
    else:
        map_list[y][x]="🥔"    
    prt_map(map_list)
```

## 2、地雷の数
皆さんはマインスイーパのことご存知ですか

数字があらわしているのは、周囲にある💣の数です。
今回は、一つ地雷原を定義しておきましたので、
各マスの周囲にある💣を計算して表示させてみましょう。

地雷原：
```python=
minefield = [
    ["?",'*',"?",'*'],
    ['*','*',"?",'*'],
    ["?","?",'*', "?"],
    ["?","?","?", "?"]]   
```

### 出力例：
```
before:
? * ? * 
* * ? * 
? ? * ? 
? ? ? ? 

after:
3 * 4 * 
* * 5 * 
2 3 * 2 
0 1 1 1 
```
code:

```python=
def check_mine(i,j):
    if i<0 or j<0:
        return 0
    elif i>=len(minefield):
        return 0
    elif j>=len(minefield[i]):
        return 0
    elif minefield[i][j]=="*":
        return 1
    else:
        return 0  

minefield = [
    ["?",'*',"?",'*'],
    ['*','*',"?",'*'],
    ["?","?",'*', "?"],
    ["?","?","?", "?"]]

print("before:")
for i in minefield:
    for j in i:
        print(j,end=" ")
    print()
print("\nafter:")
for i in range(len(minefield)):
    for j in range(len(minefield)):
        if minefield[i][j]=="*":
            print("*",end=" ")
        else:
            mine_num=0
            mine_num+=check_mine(i - 1, j - 1)#左上
            mine_num+=check_mine(i - 1, j)#真上
            mine_num+=check_mine(i - 1, j + 1)#右上
            mine_num+=check_mine(i, j - 1)#左
            mine_num+=check_mine(i, j + 1)#右
            mine_num+=check_mine(i + 1, j - 1)#左下
            mine_num+=check_mine(i + 1, j)#真下
            mine_num+=check_mine(i + 1, j + 1)#右下
            print(mine_num, end=" ")
            
            
        if (j+1)%4==0:
            print()
```
