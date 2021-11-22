h,m =input().split(":")
h=int(h)
m=int(m)

if (h-8)<0:
    h=(h-8)+24
    print("{}:{}".format(h,m))
else:
    h=h-8
    print("{}:{}".format(h,m))
