#stack class
class FixedStack:
    #空のstackに対して、popが呼ばれたら送出する例外
    def Empty(Exception):
        pass
    #満杯のstackに対して、pushが呼ばれたら送出する例外
    def Full(Exception):
        pass
    
    def __init__(self,capacity:int = 4) ->None:
        self.stk=[None]*capacity#stackの本体
        self.capacity=capacity#stackの量
        self.ptr=0#スタックのポインター
    
    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr<=0
    
    def is_full(self):
        #決まった量より多い
        return self.ptr >= self.capacity
    
    def push(self,value):
        if self.is_full():
            return self.Full()
        self.stk[self.ptr]=value
        self.ptr+=1
    
    def pop(self):
        if self.is_empty():
            return self.Empty()
        self.ptr-=1
        return self.stk[self.ptr]

def check(x,y):
    while x!= 8 or y!=2:
        #前進できるなら前進し、前進した場所を9にする。
        #上
        if meiro2[x-1][y] == 0:
            stak.push([x-1,y])
            meiro2[x-1][y]=9
            x-=1
        #下
        elif meiro2[x+1][y]==0:
            stak.push([x+1,y])
            meiro2[x+1][y]=9
            x+=1
        #左
        elif meiro2[x][y-1]==0:
            stak.push([x,y-1])
            meiro2[x][y+-1]=9
            y-=1
        #右
        elif meiro2[x][y+1]==0:
            stak.push([x,y+1])
            meiro2[x][y+1]=9
            y+=1
        #前進できないなら、スタックからpopすることで直前の座標を出す（後退）
        else:
            loc=stak.pop()
            x=loc[0]
            y=loc[1]
        if x==8 and y==2:
            meiro[8][2]="x"
            
        for i in meiro2:
            print(i)
        print()
    
            

meiro=[[1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,1,1,1,1,1,1,1,1],
       [1,1,1,0,1,1,0,0,0,0,1,1],
       [1,1,1,0,1,1,0,1,1,0,1,1],
       [1,1,1,0,0,0,0,1,1,0,1,1],
       [1,1,1,0,1,1,0,1,1,0,1,1],
       [1,1,1,0,1,1,0,1,1,0,1,1],
       [1,1,1,1,1,1,0,1,1,0,1,1],
       [1,1,0,0,0,0,0,0,1,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]]

meiro2=meiro.copy()

size=len(meiro)*len(meiro[0])
stak=FixedStack(size)
end=[8,10]
check(1,1)