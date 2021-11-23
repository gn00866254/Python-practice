def covrt_to_int(t_list):
    for i in range(len(t_list)):
        t_list[i]=eval(t_list[i])

num=int(input("input n:"))

for i in range(num):
    data_list=input("data:").split()
    covrt_to_int(data_list)
    print("max - min: {:.2f}".format(max(data_list)-min(data_list)))
