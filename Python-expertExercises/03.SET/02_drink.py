studentA = set(["玫瑰紅茶", \
               "咖啡凍紅茶", \
               "梅子紅茶", \
               "烏龍紅茶", \
               "伯爵紅茶", \
               "百香果紅茶", \
               "椰果紅茶", \
               "QQ紅茶", \
               "布丁紅茶"])
studentB = set(["梅子紅茶", \
               "蜂蜜紅茶", \
               "QQ紅茶", \
               "布丁紅茶", \
               "椰果紅茶", \
               "薄荷紅茶", \
               "玫瑰紅茶", \
               "珍珠紅茶", \
               "檸檬紅茶"])
studentC = set(["椰果紅茶", \
               "檸檬紅茶", \
               "波霸紅茶", \
               "奶香紅茶", \
               "QQ紅茶", \
               "蜂蜜紅茶", \
               "梅子紅茶", \
               "藍莓凍紅茶", \
               "烏龍紅茶"])

print("共同の好み：", studentA & studentB & studentC)
print("それぞれの好み：", studentA ^ studentB ^ studentC - (studentA & studentB & studentC))