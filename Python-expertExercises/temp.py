n=int(input())
game_list=[]
for i in range(n):
    string=input()
    for j in string:
        game_list.append(int(j))

#game_list=[1,3,1,4,1,2,1,3,2,1,3,4,3,1,2,4]
max_len=0
lengh=1
l=[]
swipe_quatity=[-(n+1),-n,-(n-1),1,(n+1),n,(n-1),-1]
for position in range(len(game_list)):
    for i in swipe_quatity:
        lengh=1
        temp_index=position+i
        if temp_index<0 or temp_index>len(game_list)-1:
            continue
        elif game_list[temp_index]==game_list[position]+1 or game_list[temp_index]==game_list[position]-1:
            lengh+=1
            while True:
                origin_temp = temp_index
                temp_index+=i
                if temp_index<0 or temp_index>len(game_list)-1:
                    break
                elif i==-1 and temp_index%n==0:
                    if game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                        lengh+=1
                    break
                elif i==1 and temp_index%(n-1)==0:
                    if game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                        lengh+=1
                    break
                elif game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                    lengh+=1
                    print(i)
        if i==swipe_quatity[0]:
            max_len=lengh
        elif max_len<lengh:
            max_len=lengh
        
"""
game_list=[1,3,1,4,1,2,1,3,2,1,3,4,3,1,2,4]
index=0
max_len=0
lengh=1
swipe_quatity=[-5,-4,-3,1,5,4,3,-1]
#swipe_quatity=[5]
for i in swipe_quatity:
    lengh=1
    temp_index=index+i
    if temp_index<0 or temp_index>15:
        continue
    elif game_list[temp_index]==game_list[index]+1 or game_list[temp_index]==game_list[index]-1:
        lengh+=1
        while True:
            origin_temp = temp_index
            temp_index+=i
            if temp_index<0 or temp_index>15:
                break
            elif game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                lengh+=1
    if i==-5:
        max_len=lengh
    elif max_len<lengh:
        max_len=lengh
            
"""

"""
origin_temp = temp_index,temp_index+=i
            if temp_index<0 or temp_index>15:
                break
            elif game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                lengh+=1
                
origin_temp = temp_index,temp_index+=i
            if temp_index<0 or temp_index>15:
                break
            elif game_list[temp_index]==game_list[origin_temp]+1 or game_list[temp_index]==game_list[origin_temp]-1:
                lengh+=1
"""