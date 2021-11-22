n,r=map(int,input().split())#箱の数n, ボールの半径r 
diameter = 2*int(r)#直径

boxes=[]
result=[]

for i in range(n):
    boxes.append(input().split())#ボックス三辺を入力する

for box in boxes:
    jump=False
    for length in box:#boxの三辺をリストから取り出し判定する
        if diameter>int(length):#もし取り出した辺は直径より大きいだったら jumpをTrueにする。
            jump=True
            break
    if jump:#Trueということは、ボール入らないからcontinueする。
        continue
    result.append(boxes.index(box))

for i in result:
    print(i+1)   
