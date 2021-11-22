S = input()

alpha=["a","e","i","o","u","A","E","I","O","U"]
for j in alpha:
    #取り除く
    S_output=S.replace(j,"")
    S=S_output

print(S)
