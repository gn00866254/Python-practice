pho_dic={"0":12,"1":3,"2":4,"3":5,"4":6,
        "5":7,"6":8,"7":9,"8":10,"9":11}

s=input().replace("-","")
ans=0
for i in s:
    ans+=int(pho_dic[i])
print(ans*2)
