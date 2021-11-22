N1,M1 = input().split()

N=int(N1)
M=int(M1)

if N%2 == 1 and M %2 ==0:
    print("YES")
elif N%2 == 0 and M %2 ==1:
    print("YES")
else:
    print("NO")
