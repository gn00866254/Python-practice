n=int(input())
#850 000
total=0
for i in range(n):
    money=int(input())
    if money>1500000:
        copy_m=money-1500000
        total+=int(copy_m*0.4)
        total+=215000
    elif money>750000:
        copy_m=money-750000
        total+=int(copy_m*0.2)
        total+=65000
    elif money>100000:
        copy_m=money-100000
        total+=int(copy_m*0.1)
print(total)
