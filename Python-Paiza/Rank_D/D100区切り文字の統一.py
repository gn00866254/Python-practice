
s = input()

underscore=s.count("_")
haifu = s.count("-")

if (underscore > haifu) or (underscore == haifu):
    print(s.replace("-","_"))
else:
    print(s.replace("_","-"))
