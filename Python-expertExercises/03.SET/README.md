# set - HomeWork

## 問題1：授業選択
某大学で生徒Aと生徒Bが授業コースの選択をしようとしています。
本日が授業選択の最終日なので二人共急いで授業内容等を確認しながら選択していたため、授業を重複して選択したものも含まれています。
生徒AとBが選択した全ての授業はそれぞれ以下の通り：

| 生徒A | 生徒B |
| -------- | -------- |
| 国語 | 微積分B |
| 物理 | 数学 |
| コンピューター概論 | 微積分B |
| 微積分A | 国語 |
| 物理 | 数学 |
| 国語 | プログラミング |
| 微積分A | 物理 |
| プログラミング | 国語 |
| 国語 | 電子回路 |
| 物理 | 微積分B |
| コンピューター概論 | プログラミング |

先ずはそれぞれ選択したもの**全てを格納**しその後から処理を行い次の出力表示を完成させてください。

* AとBが選択した全てのコースを表示させること（授業コースは重複してはならない）

* AとBが共同選択したコースを全て表示させること

* AとBの内、片方のみ選択しているコースを全て表示させること

* 1週間後、生徒Aは自分には向いていない科目を履修しているので、「物理」「微積分A」を取り消そうと考えています。前述の2科目を取り消した場合、AとBが共同選択したコースはどの様になるでしょうか？「(2)」と同様のフォーマットで表示させること。

* 生徒Bはまだ追加履修する余裕があると思っているので、新たに「コンピューター概論」を追加しようと考えています。AとBの内、片方のみ選択しているコースはどの様になるでしょうか？「(3)」と同様のフォーマットで表示させること。

* 生徒Aと生徒Bの友達「生徒C」がお互いの履修している科目が共通しているかどうか知りたいようです。生徒Cが履修している科目は「中国語基礎」「中日翻訳」「中国歴史概説」「数学」「中国語演習」「プログラミング」です。生徒A、生徒B、生徒Cが全員共同で履修している科目はどれらでしょうか？「(2)」と同様のフォーマットで表示させること。


### 出力例
```
生徒A： {'コンピューター概論', '国語', 'プログラミング', '物理', '微積分A'}
生徒B： {'国語', 'プログラミング', '微積分B', '物理', '数学', '電子回路'}
共同選択した授業: {'プログラミング', '物理', '国語'}
別々で選択した授業: {'数学', '微積分A', 'コンピューター概論', '電子回路', '微積分B'}

共同選択した授業: {'プログラミング', '国語'}
別々で選択した授業: {'数学', '電子回路', '微積分B', '物理'}

共同選択した授業: {'プログラミング'}
```
Code:
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/03.SET/01_subject_select.py)

## 問題２：飲み物の種類
3人の学生がいてそれぞれを「学生A」、「学生B」、「学生C」としましょう。
台湾の某飲料店で買いたいと考えています。
この3人は皆紅茶が好きなので、紅茶の部分だけを見ようと思いました。
紅茶のメニューはこれらの種類があります（実際のメニューから一部抜粋）：

| 紅茶の種類 | | | |
| -------- | -------- | -------- | -------- |
| 伯爵紅茶 | 梅子紅茶 | 蜂蜜紅茶 | 波霸紅茶 |
| 珍珠紅茶 | 椰果紅茶 | 薄荷紅茶 | 檸檬紅茶 |
| 玫瑰紅茶 | 優酪紅茶 | 布丁紅茶 | 冬瓜紅茶 |
| 烏龍紅茶 | QQ紅茶 | 奶香紅茶 | 多多紅茶 |
| 仙草凍紅茶 | 藍莓凍紅茶 | 百香果紅茶 | 咖啡凍紅茶 |

学生A～Cがそれぞれ好きな種類は次の通りです。
| 学生A | 学生B | 学生C |
| -------- | -------- | -------- |
| 玫瑰紅茶 | 梅子紅茶 | 椰果紅茶 |
| 咖啡凍紅茶 | 蜂蜜紅茶 | 檸檬紅茶 |
| 梅子紅茶 | QQ紅茶 | 波霸紅茶 |
| 烏龍紅茶 | 布丁紅茶 | 奶香紅茶 |
| 伯爵紅茶 | 椰果紅茶 | QQ紅茶 |
| 百香果紅茶 | 薄荷紅茶 | 蜂蜜紅茶 |
| 椰果紅茶 | 玫瑰紅茶 | 梅子紅茶 |
| QQ紅茶 | 珍珠紅茶 | 藍莓凍紅茶 |
| 布丁紅茶 | 檸檬紅茶 | 烏龍紅茶 |

この3人の学生から次の情報を整理して結果を表示すること。
1. 全員が共同で好きな種類の紅茶
2. 好きな種類がそれぞれ独立している紅茶

### 表示例:
```
共同の好み： {'QQ紅茶', '椰果紅茶', '梅子紅茶'}
それぞれの好み： {'百香果紅茶', '珍珠紅茶', '咖啡凍紅茶', '薄荷紅茶', '藍莓凍紅茶', '奶香紅茶', '波霸紅茶', '伯爵紅茶'}
```

Code:
[Answer](https://github.com/gn00866254/Python-expertExercises/blob/main/03.SET/02_drink.py)