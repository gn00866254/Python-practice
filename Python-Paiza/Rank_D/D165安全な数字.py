# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()

outsideloop = True
for i in s:
    if outsideloop:
        count = 0
        for j in range(4):
            if i == s[j]:
                count+=1
                if count > 1:
                    outsideloop=False
                    break
    else:
        break

if count >1:
    print("NG")
else:
    print("OK")
