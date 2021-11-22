x_1,y_1,p_1=input().split()
x_2,y_2,p_2=input().split()

x1= int(p_1)/(int(x_1)*int(y_1))
x2= int(p_2)/(int(x_2)*int(y_2))

if x1<x2:
    print("{} {} {}".format(x_1,y_1,p_1))
elif x2<x1:
    print("{} {} {}".format(x_2,y_2,p_2))
elif x2==x1:
    print("DRAW")
