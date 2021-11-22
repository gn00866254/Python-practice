h_1,h_2,h_3=input().split()
dolls=[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
h1=[]
h2=[]
h3=[]
h_1=int(h_1)
h_2=int(h_2)
h_3=int(h_3)

for i in range(h_1):
    h1.append(dolls.pop(0))

for i in range(h_2):
    h2.append(dolls.pop(0))

for i in range(h_3):
    h3.append(dolls.pop(0))

print("".join(h1))
print("".join(h2))
print("".join(h3))
