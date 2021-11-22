import random
def writefile(fname):
    string=""
    f=open(fname,"w")
    #タイトルを書き込み
    title="砲弾射撃記録"
    f.write(title+"\n")
    #一回目から百回目の文字列を用意
    for i in range(100):
        string+="{}回目\t".format(i+1)
    f.write("ID\t"+string+"\n")
    #データを作成する
    for i in range(50):
        content=""
        for j in range(100):
            r_num = random.randint(50,100)
            content +=str(r_num)+"\t"
        f.write("{}\t{}\n".format(i+1,content))
    f.close()

fname="cannon.txt"
#寫檔
writefile(fname)
