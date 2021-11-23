string = input("Input:")
re_str = list(string.replace(" ", "").lower()) # "aBCd" = "abcd"

set_list = [] # 文字を格納する変数
set_list_count = []# 文字数を格納する変数

for x in re_str:
    if not x in set_list: # この文字はリストにありますか？
        set_list.append(x)
        set_list_count.append(re_str.count(x)) # LISTにあるXの数を計算します

for i in range(len(set_list)):
    print("{}/{}: {}".format(set_list[i].upper(),set_list[i] ,set_list_count[i]))
