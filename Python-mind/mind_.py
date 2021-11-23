def crt_num_list():
    start=int(input("start:"))
    end=int(input("end:"))
    return list(range(start,end))

#リストの数値を二進数にして新たなリストを返す、max長さ分0を補う。
def crt_b_list(list,maxlen)->list :
    b_list=[]
    for num in list:
        b2=format(num,"b")
        while len(b2)<maxlen:
            b2="0"+b2
        b_list.append(b2)
    return b_list

def prt_group_num(col,b2_list):
    for b2 in b2_list:
        if b2[-(col+1)]=="1":
            print(int(b2,2),end=" ")
        
#数字を格納するリスト
numList=crt_num_list()
#formatで二進数にし、max値の長さを取得。
maxlen=len(format(max(numList),"b"))
b2_list=crt_b_list(numList,maxlen)

ans=""
# 0  1  2  3
#-1 -2 -3 -4

for i in range(maxlen):
    prt_group_num(i,b2_list)
    print()
    print("このグループに入っていますか？")
    u_input=input("y or n　：　")
    if u_input == "y":
        ans+="1"
    else:
        ans+="0"

print("あなたが選んだのは",int(ans[::-1],2))
input("合っています？")