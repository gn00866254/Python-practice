s = input("please enter string: ")
#判定したい語尾
suffix = input("Please enter the suffix you want to judge: ")
#スライスで判定される文字列の語尾を切り取ります。
# if s[len(s) - len(suffix) :] == suffix:
if s[-len(suffix):] == suffix:
    print("True")
else:
    print("False")