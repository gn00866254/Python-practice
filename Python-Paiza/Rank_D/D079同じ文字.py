s=input()
c=0
for i in s:
    if s[0]!=i:
        c+=1
if c>0:
    print("OK")
else:
    print("NG")
