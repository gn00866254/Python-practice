weight,times=map(int,input().split())
fruits=[int(input()) for i in range(times)]

for i in fruits:
    if i<=weight:
        print(weight)
    elif i%weight <weight/2:
        print(i//weight*weight)
    else:
        print((i//weight+1)*weight)
