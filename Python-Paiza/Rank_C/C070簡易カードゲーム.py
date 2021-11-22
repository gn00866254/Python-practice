def string_count(string,cha):
    num=0
    for i in string:
        if i == cha:
            num+=1
    return num

def same_cards(s):
    count=0
    for cha in s:
        if string_count(s,cha) > count:
            count=string_count(s,cha)
    return count

def two_pair(s):
    return string_count(s,s[0])==2 and string_count(s,s[2])==2
        
n = int(input("How many?:"))
#何セットかを用意する
cardlist=[]
for i in range(n):
    card=input("{}セット:".format(i+1))
    cardlist.append(card)

#same_cards()
result=["No Pair","One Pair","Three Card","Four Card"]
for cards in cardlist:
    if two_pair(cards):
        print("Two Pair")
    else:
        card_num=same_cards(cards)
        print(result[card_num-1])
