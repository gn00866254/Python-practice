Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@gn00866254 
eclairsameal
/
Level-3_Python
Public
1
01
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Level-3_Python/homework20/homework20_2.py /
@eclairsameal
eclairsameal Update homework20_2.py
Latest commit 231351c on 22 Feb
 History
 1 contributor
48 lines (37 sloc)  1.74 KB
   
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:06:48 2020
@author: Fenrir
Description :
文字列が全て数字だった場合、その文字の数値全てを加算することが出来る機能を関数を用いて作成すること。
文字列が全て大文字である場合は、その文字全てを「A～Z」の順でソート出来る機能を関数と用いて作成すること。
文字列が全て小文字である場合は、その文字全てを「z～a」の順でソート出来る機能を関数と用いて作成すること。
"""
# ---------- function ----------
def number_str(s): # 文字列が全て数字だった場合
    s_list = list(s) # string -> list ("123" = ["1", "2", "3"])
    sum_val = 0
    for x in s_list: 
        sum_val += int(x) # 数値全てを加算するこ
    return sum_val

def upper_str(s): # 文字列が全て大文字である場合
    s_list = list(s) # string -> list ("ABC" = ["A", "B", "C"])
    s_list.sort() # 昇順に（小さいものから大きいものへ）並べ替える。
    return s_list

def lower_str(s): # 文字列が全て小文字である場合は
    s_list = list(s) # string -> list ("abc" = ["a", "b", "c"])
    return sorted(s_list, reverse = True) # 「reverse」にTrueを指定すると、降順に並べ替えが行われる。

def print_str(slist): #   list -> string(["a", "1", "c", "3"] = "a1c3")
    s = ""
    for x in slist:
        s += x
    return s
    
# ---------- main ----------
# while True:
string = input("Input: ")
if string.isdigit(): # 数字の判定
    print(number_str(string))
elif string.isupper(): # 大文字の判定
    print(print_str(upper_str(string)))
elif string.islower(): # 小文字の判定
    print(print_str(lower_str(string)))

    

© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
