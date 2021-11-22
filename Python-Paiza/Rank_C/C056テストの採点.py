N,M=map(int,input().split()) #人数を表す整数 N と合格点を表す整数 M
stud_list=[]#生徒の成績を格納するためのリスト
penalty=-5　#欠席したときの減点
for i in range(N):
    score,absence=map(int,input().split())#スコアと欠席回数
    score+=absence*penalty#スコアは欠席回数×減点
    #０点未満は０とみなす
    if score<0:
        score=0
    stud_list.append(score)

for i in range(len(stud_list)):
    #もしスコアは合格点以上だったら番号（index+1）で出力
    score=stud_list[i]
    if score>=M:
        print(i+1)
