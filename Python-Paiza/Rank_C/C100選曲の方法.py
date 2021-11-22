#曲の数N,何分M,何秒Sを入力する
N,M,S=map(int,input().split())
#分をすべて秒にして合計秒数を計算する
max_S=M*60+S
song=[]
for i in range(N):
    m,s=map(int,input().split())　#スペース区切りで入力した時間を処理する
    m*=60　#分数を秒数にする
    s+=m
    song.append(s)　#listに追加する

#昇順に並び替える
new_song=sorted(song)
c=0
for i in new_song:
    temp=max_S-i #合計秒数から曲の秒数を引いて、結果を変数に代入する。
    if temp<0:　#もし0以下、要は時間を超えたらbreak
        break
    max_S-=i　#なければ、秒数を引き、カウントに一を足す
    c+=1
print(c)
