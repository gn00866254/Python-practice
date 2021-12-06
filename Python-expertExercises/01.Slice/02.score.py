import random
times=int(input("Input n:"))
score_list=[]
for time in range(times):
    score_list.append(random.randint(1,100))
print("Original: {}".format(score_list))
print("Result: {}".format(sorted(score_list)[1:-1]))