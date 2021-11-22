times=int(input())
User_input = [input() for i in range(times)]
print("Hello",end=" ")
for i in range(len(User_input)-1):
    print("{},".format(User_input[i]),end="")
print("{}.".format(User_input[-1]))
