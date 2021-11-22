#アクセス
file=open("game.txt")
#幅は40+10、棒三つなので53個「-」
print("-"*53)
#一行ずつ
for lines in file:
    #行ごとにリストにし、出力する。
    line=lines.split(",")
    print("|{:<40}|{:>10}|".format(line[0],line[1].replace("\n","")))
    print("-"*53)
file.close()
