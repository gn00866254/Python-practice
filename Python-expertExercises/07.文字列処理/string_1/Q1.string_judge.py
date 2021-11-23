def input_function(input_str, len_n): # 文字列が全て数字、且長さが len_n のなっているかを判断すること
    while not(input_str.isdigit() and len(input_str) == len_n):
        input_str = input("Enter again: ")
    return input_str

def cal_age(birthday_str):
    new_year = 2021
    return new_year - (int(birthday_str)//10000) # ex: 19950101 // 10000 = 1995

# main
name = input("Please enter your name: ")
input_str = input("Please enter your birthday(ex: 20200310): ")
birthday = input_function(input_str, 8)

age = cal_age(birthday)
# print(age) # 計算が正しいかどうかを確認します

input_str = input("Please enter your Cell phone: ")
cell_phone = input_function(input_str, 11)

print("-" * 30)
print("Name:{:>25}".format(name))
print("Age:{:>26}".format(age))
print("Cell phone:{:>19}".format(cell_phone))
print("-" * 30)
