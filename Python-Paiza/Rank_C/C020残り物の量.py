#m[kg]のうち、p[%]を売る、売れ残りをお惣菜にして販売したところ、そのうち q[%] が売れた。
m,p,q=input().split()
m,p,q=int(m),int(p),int(q)

sellout= m-m*(p/100)  #m[kg]のうち、p[%]を売る
remain = sellout-sellout*(q/100)

print("{}".format(remain))#売れ残った量 [kg] 
