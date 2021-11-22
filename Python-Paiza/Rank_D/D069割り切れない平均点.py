score=0
average=0
n = input().split()
for i in n:
    score+=int(i)
average = score/len(n)
print("{:.1f}".format(average))
