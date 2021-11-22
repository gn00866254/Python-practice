import math
def rank(score):
    if 0<=score<60:
        return "D"
    elif score<70:
        return "C"
    elif score<80:
        return "B"
    elif score<=100:
        return "A"


#学生の人数を表す整数 k、レポートの問題数を表す整数 n
k,n=map(int,input().split())
q_score=100/n
score=0
result=[]
for i in range(k):
    #提出した日を表す変数と、正解した問題数を表す変数
    day,q_num=map(int,input().split())
    if day>=10:
        score=0
    elif day>=1 and day<=9:
        score=math.floor(q_num*q_score*0.8)
    else:
        score=q_num*q_score
    
    student_rank=rank(score)
    print(student_rank)
    
