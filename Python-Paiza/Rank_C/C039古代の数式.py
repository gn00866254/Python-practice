def puzzle(E_part):
    ans=0
    #< :10 /:1 なので、数えてかけること。
    ans= E_part.count("<")*10+E_part.count("/")*1
    return ans
 
ans=0
#+の記号を取り除く
E=input().replace("+","")
ans=puzzle(E)
print(ans)
