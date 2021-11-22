def monTable(contents):
    name,atk,defen=[],[],[]
    for i in contents:
        monData=i.split()
        name.append(monData[0])
        atk.append(monData[1])
        defen.append(monData[2])
    return name,atk,defen

#アクセス
file=open("monster.txt")
file.readline()
title=file.readline()
contents = file.readlines()
file.close()
#タイトルを表示する。
print(title[:-1])
#モンスターを表示する。
num=0
for i in contents:
    print("{}.{}".format(num+1,i[:-1]))
    num+=1

#指定する。
index=int(input("どれが見たい？"))
#文字列を処理して、数値を抽出する。
name,atk,defen = monTable(contents)
#指定したモンスターのデーターを変数に格納。
sName=name[index-1]
sAtk=int(atk[index-1])
sDefen=int(defen[index-1])
sAve=(sAtk+sDefen)/2
#出力する。
print("Name:{} , Atk: {} , Def: {} ,Ave: {:.2f}".format(sName,sAtk,sDefen,sAve))
    
