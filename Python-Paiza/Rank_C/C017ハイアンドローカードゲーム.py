#親カードの1つ目の番号は a、2つ目の番号は b で表されます。
a,b=input().split()
a,b=int(a),int(b) 
#何回比べるか
times=int(input())
result=[]
for i in range(times):
    a_1,b_1=input().split() #カードの情報
    a_1,b_1=int(a_1),int(b_1)
    #一枚目の比較
    if (a==a_1 and b<b_1) or (a > a_1):
        result.append("High")
    #二枚目の比較
    elif (a==a_1 and b>b_1) or (a<a_1):
        result.append("Low")
        
print("\n".join(result))
