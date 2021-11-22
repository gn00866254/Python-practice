#変更前の文章表示部分の高さ、横幅を表す整数 H, W 変更後の文章表示部分の横幅を表す整数 X
h,w,x=input().split()
#文字列を定義し、入力したものをすべてこの文字列で表す。
string=""
for i in range(int(h)):
    s=input()
    string=string+s
#変更後の幅の倍数になったら改行させる。
for i in range(len(string)):
    if (i+1)%int(x)==0:
        print(string[i])
        continue
    print(string[i],end="")
