#くじの当選番号6つ
bingo=input().split()
#くじの数
n=int(input())

for i in range(n):
    bingo_num=0
    lottery_num=input().split()#くじの番号を入力
    for num in lottery_num:
        if num in bingo: #もしくじの番後は当選番号にあるなら,bingo_numに１を足す
            bingo_num+=1
    print(bingo_num)
