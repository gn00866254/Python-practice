A,B,C = input().split()
Acost=int(A)
Bcost=int(B)
Ccost=int(C)

beefList = [Acost,Bcost,Ccost]
beefList.sort()

print(beefList[1])
