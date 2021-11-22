file=open("game.txt")
num=int(input("何行目まで出力しますか："))
for i in range(num):
    print(file.readline())
file.close()
