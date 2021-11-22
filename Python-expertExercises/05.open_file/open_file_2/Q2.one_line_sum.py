file=open("score.txt")
score=[i for i in file]
newscore=[int(i) for i in score[:-1]]
print("総和：{}".format(sum(newscore)))
