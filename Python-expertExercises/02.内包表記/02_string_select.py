s = input("input string:").split()  # python algorithm java android google

select_index = []
for i in range(len(s)):
    word=s[i]#単語
    n = int(input("Select a character in the {}: ".format(word)))
    #範囲を超えると、もう一度入力
    while n >= len(word) or n < 0:
        n = int(input("Enter again: "))
    select_index.append(n)

print("Selected character index: {}".format(select_index))
select_char = [s[i][select_index[i]] for i in range(len(s))]
print("Selected character elements:", select_char)