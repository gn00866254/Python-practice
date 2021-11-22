# coding: utf-8
daytime=input().replace(" ","")

length=len(daytime)
w_count=daytime.count(daytime[0])
if length==w_count:
    print("Yes")
else:
    print("No")


"""
#old version
m,d = input().split()
M=map(int, str(m))
D=map(int, str(d))

Mlist=list(M)
Dlist=list(D)


if len(Dlist)<2 and len(Mlist)<2:
    if Mlist[0] == Dlist[0] :
        print('Yes')
    else:
        print('No')
elif len(Dlist)<2 and len(Mlist)<3:
    if Mlist[0] == Dlist[0] and Mlist[1] == Dlist[0]:
        print('Yes')
    else:
        print('No')
elif len(Dlist)<3 and len(Mlist)<2:
    if Mlist[0] == Dlist[1] and Mlist[0] == Dlist[0]:
        print('Yes')
    else:
        print('No')
elif len(Dlist)<3 and len(Mlist)<3:
    if Mlist[1] == Dlist[1] and Mlist[0] == Dlist[1] and Mlist[0] == Dlist[0] and Mlist[0] == Dlist[0] and Mlist[1] == Dlist[0] and Mlist[1] == Dlist[0] and Mlist[1] == Dlist[1] and Mlist[1] == Dlist[1]:
        print('Yes')
    else:
        print('No')
        
"""
