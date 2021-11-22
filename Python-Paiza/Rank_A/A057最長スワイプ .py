def path_steps(p_i, p_j, d, step):
    """ 計算可走路徑的步數 """
    while val:= n_array[p_i + d[0]][p_j + d[1]]: 
        if val == -1 or val != (n_array[p_i][p_j] + 1):
            break
        else:
            step+=1
            p_i, p_j = p_i + d[0], p_j + d[1]
    return step

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1),(1, 0),(1, 1)]    

n = int(input())
n_array = [[-1 for i in range(n+2)] for j in range(n+2)]

for i in range(1, n+1):        
    n_array[i][1:n+1] = list(map(int, list(input())))
        
max_step = 1
all_step = []

for i in range(1, n+1):
    for j in range(1, n+1):
        path_dis = [d for d in direction if n_array[i+d[0]][j+d[1]] == (n_array[i][j]+1)]
        for pd_i, pd_j in path_dis:
            temporary_step = 2
            all_step.append(path_steps(i + pd_i, j + pd_j, (pd_i, pd_j), temporary_step))
if all_step:
    max_step = max(all_step)
print(max_step)

"""
#version1
n=int(input())
game_list=[]
for i in range(n):
    string=input()
    for j in string:
        game_list.append(int(j))

#game_list=[1,3,1,4,1,2,1,3,2,1,3,4,3,1,2,4]
max_len=0
lengh=1
all_len=[]
move_on=False
#左上 左下 左 上  下 右上 右 右下
swipe_quatity=[-(n+1),(n-1),-1,-n,n,-(n-1),1,(n+1)]
for position in range(len(game_list)):
    for i in swipe_quatity:
        lengh=1
        temp_index=position+i
        if temp_index<0 or temp_index>len(game_list)-1:
            continue
        elif (i==-1 and position%n==0) or (i==1 and position%n-1==0):
            continue
        elif (i in swipe_quatity[:3] and position%n==0) or (i in swipe_quatity[-3::] and position%n-1==0):
            continue
        elif i==-1 and temp_index%n==0:
            if game_list[temp_index]==game_list[position]+1 or game_list[temp_index]==game_list[position]-1:
                lengh+=1
            continue
        elif i==1 and temp_index%(n-1)==0:
            if game_list[temp_index]==game_list[position]+1 or game_list[temp_index]==game_list[position]-1:
                lengh+=1
            continue
        elif game_list[temp_index]==game_list[position]+1:
            lengh+=1
            move_on=True
            move=1
        elif game_list[temp_index]==game_list[position]-1:
            lengh+=1
            move_on=True
            move=-1
            
        while move_on:
            origin_temp = temp_index
            temp_index+=i
            if temp_index<0 or temp_index>len(game_list)-1:
                move_on=False
            elif i==-1 and temp_index%n==0:
                if game_list[temp_index]==game_list[origin_temp]+move:
                    lengh+=1
                move_on=False
            elif i==1 and temp_index%(n-1)==0:
                if game_list[temp_index]==game_list[origin_temp]+move:
                    lengh+=1
                move_on=False
            elif game_list[temp_index]==game_list[origin_temp]+move:
                lengh+=1
            else:
                move_on=False
        all_len.append(lengh)
print(max(all_len))
"""
    
