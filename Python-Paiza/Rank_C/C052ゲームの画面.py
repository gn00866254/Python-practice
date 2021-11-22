numx,numy=map(int,input().split())
gox,goy=map(int,input().split())

# (30 × 240) + (30 × 180) - (30 × 30) = 11700 
print(abs(goy*numx)+abs(gox*numy)-abs(gox*goy))
