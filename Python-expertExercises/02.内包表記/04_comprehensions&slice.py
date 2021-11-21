words=['aaation', 'bbbtion', 'ccbtionshh', 'bbs', 'jjtion']
#後ろの四文字がtionであれば、うしろの四文字を切り取った要素に"s"を足し、追加する
print([ word[:len(word)-4]+"s" for word in words if word[-4:]=="tion"])