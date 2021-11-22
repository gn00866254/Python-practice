#ファイルアクセス
file=open("game.txt")
#ゲーム値段表
gamedict={}
file.readline() #一行目を読み込み。

for lines in file:
    #行ごとに読み込み、リストの要素をそれぞれの変数に格納。
    line=lines.split(",")
    gameName,price=line[0],int(line[1].replace("\n",""))
    #変数をそれぞれ辞書のキーと値として辞書に追加・
    gamedict[gameName]=price
file.close()

#一番高いのと一番安い
expensive=max(gamedict.values())
cheap=min(gamedict.values())
#もし値が一番高い値段と一致していればキーを出力。反対に、安いときは安いゲームのキーを。
for k,v in gamedict.items():
    if v==expensive:
        print("The most expensive is {}".format(k))
    elif v==cheap:
        print("The cheapest is {}".format(k))
