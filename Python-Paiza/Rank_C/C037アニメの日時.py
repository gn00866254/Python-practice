string=input()
month=string[:2]
daytime=int(string[3:5])
time=int(string[-5:-3])
minu=string[-2:]
#２４時を超えたら、商を求め、日付に足す。
if time>=24:
    daytime+=time//24
    time=time%24#あまりを求め時間にする。
  
#もし日付や時間が10未満だったら0を付ける
if time<10:
   time="0"+str(time)
if daytime < 10:
   daytime="0"+str(daytime)
   
print("{}/{} {}:{}".format(month,daytime,time,minu))
