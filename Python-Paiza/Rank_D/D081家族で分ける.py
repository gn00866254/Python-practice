N = int(input())
H,W = input().split()
candy = int(H) * int(W)
ans = candy%N

print(ans)
