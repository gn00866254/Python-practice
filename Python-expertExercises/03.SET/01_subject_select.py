studentA = {"国語", "物理", "コンピューター概論", "微積分A", "物理",\
            "国語", "微積分A", "プログラミング", "国語", "物理", "コンピューター概論"}   
studentB = {"微積分B", "数学", "微積分B", "国語", "数学",\
            "プログラミング", "物理", "国語", "電子回路", "微積分B", "プログラミング"}
print("生徒A：", studentA)
print("生徒B：", studentB)
print("共同選択した授業:", studentA & studentB)
print("別々で選択した授業:", studentA ^ studentB)
print()
#削除
studentA.remove("物理")
studentA.remove("微積分A")
#共同選択した授業
print("共同選択した授業:", studentA & studentB)
#生徒Bの追加
studentB.add("コンピューター概論")
print("別々で選択した授業:", studentA ^ studentB)
print()
studentC = {"中国語基礎", "中日翻訳", "中国歴史概説", "数学", "中国語演習", "プログラミング"}
print("共同選択した授業:", studentA & studentB & studentC)