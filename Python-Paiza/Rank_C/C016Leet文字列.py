#置き換える前と置き換える語の文字をペアーとして辞書にする。
alpha_rule = {'A': 4, 'E': 3, 'G': 6 ,
              'I': 1,'O': 0,'S':5,"Z": 2 }

s = input()
for i in s :
    if i in alpha_rule :
        print(alpha_rule[i],end="")
    else:
        print(i,end="")
