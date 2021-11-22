h,w = map(int,input().split())
"""
画素値が 128 以上 : 1 (白)
画素値が 127 以下 : 0 (黒)
"""
for i in range(h):
    result=[]
    imagePixels=list(map(int,input().split()))
    for j in range(w):
        if imagePixels[j]<=127 and imagePixels[j]>=0:
            result.append("0")
        elif imagePixels[j]>=128:
            result.append("1")
    print(" ".join(result))
