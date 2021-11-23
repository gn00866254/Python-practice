string = "The Zen of Python, by Tim Peters\n\
Beautiful is better than ugly.\n\
Explicit is better than implicit.\n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Special cases aren't special enough to break the rules.\n\
Although practicality beats purity.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!"

before_encryption_list = [] # 暗号化前
after_encryption_list = [] # 暗号化後
before_encryption_count_list = [] 
# print(string)

n = int(input("Please enter a few words you want to encrypt(暗号化したい単語をいくつか入力してください): "))
for i in range(n):
    before_encryption_list.append(input("Before encryption(暗号化前): "))
    after_encryption_list.append(input("After encryption(暗号化後): "))    
    before_encryption_count_list.append(string.count(before_encryption_list[i]))

print("-" * 60)
print("{:<25}{:<25}{:<10}".format("Before encryption", "After encryption", "Counts"))
for i in range(n): 
    print("{:<25}{:<25}{:<10}".format(before_encryption_list[i], after_encryption_list[i], before_encryption_count_list[i]))
print("-" * 60)

for i in range(n): 
    string = string.replace(before_encryption_list[i], after_encryption_list[i])
print(string)
