import random
#読込
filename="jackpot_language.txt"
file=open(filename)
langList=file.readline().strip().split(",")
#['English', '日本語']言語の選択肢
for i in range(len(langList)):
    print("{}.{}".format(i+1,langList[i]),end=" ")
choiceLang=int(input("Which one?"))

#内容の改行文字を消して、区切り文字で分割してから選んだ言語に対応する内容をリストに格納。
detail=[ i.strip().split(",")[choiceLang-1] for i in file]
#内容をそれぞれの変数に格納。
starText=detail[0]
endText=detail[1]
copletMessa=detail[2]
countText=detail[3]
gameStart=detail[4]
playText=detail[5]
overText=detail[6]
jackpotText=detail[7]
winText=detail[8]
lostText=detail[9]
file.close()

start=int(input(starText))
end=int(input(endText))
jackpot = random.randint(start,end)
print(copletMessa)

count = int(input(countText))
print("「-----"+gameStart+"-----」")
for c in range(count):
    print(playText.format(start,end))
    guess=int(input(str(c+1)+"："))
    if guess<start or guess>end:
        print(overText.format(start,end))
    elif guess == jackpot:
        print(jackpotText.format(jackpot)+winText)
        break
    #もし入力した数字がjackpotより大きい場合、
    #入力した数字を新たなendにする。
    #反対に小さい場合は、startにする。
    elif guess>jackpot:
        end=guess
    elif guess<jackpot:
        start=guess
    print("--------------------------")
#全部試して当たらなかったらmessageを出力する。
else:
    print(lostText)
    print(jackpotText.format(jackpot))
