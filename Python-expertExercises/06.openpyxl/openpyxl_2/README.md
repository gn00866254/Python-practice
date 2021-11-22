# Python - Openpyxl（3） - Exercise(解答)
###### tags: `Python HomeWork`



## 問題1：sheet2枚やっちゃおう！
以下の「pcr_positive.xlsx」ファイルをダウンロードし、スクリプトファイルと同じフォルダの中に入れましょう。
[pcr_positive.xlsx](https://docs.google.com/spreadsheets/d/1GDH2_6wWpMRG0VlMIgZpm1gM_tyCkWfe/edit?usp=sharing&ouid=117199946690276012800&rtpof=true&sd=true)

以上のワークブックを読込、
それぞれのシートオブジェクトと陽性者人数を出力してください。


```
出力例１：
<Worksheet "pcr_positive_daily1">
陽性者： 62110
<Worksheet "pcr_positive_daily2">
陽性者： 5057906
```
code：
```python=
import openpyxl
wb=openpyxl.load_workbook("pcr_positive.xlsx",data_only=True)
#7/1-7/23
for sheet in wb:
    print(sheet)
    total=0
    for row in sheet.iter_rows(min_row=2):
        total+=row[1].value
    print("陽性者：",total)
```


## 問題2：観光名所
[観光名所](https://docs.google.com/spreadsheets/d/17xiPrb4kr3RX9Xf_lZyVvvDwnqz3mkuq/edit?usp=sharing&ouid=117199946690276012800&rtpof=true&sd=true)

以上のファイルをダウンロードし、
読み込んだ後、名所と住所とURLを表示してください。

```
出力：
-------------
観光名称： 名称
住所： 住所
URL: URL
-------------
観光名称： 都立清澄庭園
住所： 東京都江東区清澄3-3-9 
URL: https://www.tokyo-park.or.jp/teien/contents/index033.html
-------------
観光名称： 深川江戸資料館
住所： 東京都江東区白河1-3-28
URL: https://www.kcf.or.jp/fukagawa/
-------------
観光名称： 芭蕉記念館
住所： 東京都江東区常盤1-6-3
URL: https://www.kcf.or.jp/basho/
-------------
観光名称： 東京都現代美術館
住所： 東京都江東区三好4-1-1
URL: https://www.mot-art-museum.jp/
-------------
観光名称： 中川船番所資料館
住所： 東京都江東区大島9-1-15
URL: https://www.kcf.or.jp/nakagawa/
-------------
観光名称： 日本科学未来館
住所： 東京都江東区青海2-3-6
URL: https://www.miraikan.jst.go.jp/
-------------
観光名称： 深川東京モダン館
住所： 東京都江東区門前仲町1-19-15
URL: http://fukagawatokyo.com/
-------------
観光名称： 亀戸梅屋敷
住所： 東京都江東区亀戸4-18-8
URL: https://www.kameume.com/
-------------
観光名称： 豊洲市場
住所： 東京都江東区豊洲6-6-1
URL: http://www.toyosu-market.or.jp/
-------------
観光名称： 明治丸
住所： 東京都江東区越中島2-1-6
URL: https://www.kaiyodai.ac.jp/overview/facilities/meijimaru.html
-------------
観光名称： 夢の島熱帯博物館
住所： 東京都江東区夢の島2-1-2
URL: http://www.yumenoshima.jp/index.html
-------------
観光名称： 東京都虹の下水道館
住所： 東京都江東区有明2-3-5
URL: https://www.nijinogesuidoukan.jp/
-------------
観光名称： 東京都立第五福竜丸展示館
住所： 東京都江東区夢の島2-1-1
URL: http://d5f.org/
-------------
観光名称： 東京都水の科学館
住所： 東京都江東区有明3-1-8
URL: http://www.mizunokagaku.jp/
-------------
観光名称： 東京臨海部広報展示室 TOKYO ミナトリエ
住所： 東京都江東区青海2-4-24
URL: http://www.tokyoport.or.jp/minatorie/index.html
-------------
観光名称： 東京ビッグサイト
住所： 東京都江東区有明3-10-1
URL: http://www.bigsight.jp/
-------------
観光名称： 田河水泡・のらくろ館
住所： 東京都江東区森下3-12-17
URL: https://www.kcf.or.jp/morishita/josetsu/norakuro/
-------------
観光名称： 石田波郷記念館
住所： 東京都江東区北砂5-1-7
URL: https://www.kcf.or.jp/sunamachi/josetsu/ishida/
-------------
観光名称： 伊東深水と関根正二紹介展示コーナー
住所： 東京都江東区森下3-12-17
URL: https://www.kcf.or.jp/morishita/josetsu/ito-sekine/
-------------
観光名称： 小津安二郎紹介展示コーナー
住所： 東京都江東区古石場2-13-2
URL: https://www.kcf.or.jp/furuishiba/josetsu/ozu/
-------------
観光名称： 工匠館
住所： 東京都江東区森下3-12-17
URL: https://www.city.koto.lg.jp/103020/bunkasports/bunka/dento/6369.html
-------------
観光名称： 旧大石家住宅
住所： 東京都江東区南砂5-24
URL: https://www.city.koto.lg.jp/103020/bunkasports/bunka/oishike/6374.html
-------------
観光名称： 横綱大鵬顕彰コーナー
住所： 東京都江東区白河1-3-28
URL: https://www.kcf.or.jp/fukagawa/outline/taiho/
-------------
観光名称： 水素情報館　東京スイソミル
住所： 東京都江東区潮見1-3-2
URL: https://www.tokyo-suisomiru.jp/
-------------
観光名称： そなエリア東京
住所： 東京都江東区有明3-8-35
URL: http://www.tokyorinkai-koen.jp/

```

code：
```python=
import openpyxl
wb=openpyxl.load_workbook("kotocity_tourism.xlsx",data_only=True)
ws=wb["kotocity_tourism"]
for row in ws:
    print("-"*13)
    print("観光名称：",row[4].value)
    print("住所：",row[8].value)
    print("URL:",row[28].value)
```


## 問題3：探してみようぜ！
[観光名所](https://docs.google.com/spreadsheets/d/17xiPrb4kr3RX9Xf_lZyVvvDwnqz3mkuq/edit?usp=sharing&ouid=117199946690276012800&rtpof=true&sd=true)

以上のファイルをダウンロードし、読み込みます。
次に、入力できるようにします。


```
**出力例１：**

検索：東京

結果：
-------------
観光名称： 東京都現代美術館
住所： 東京都江東区三好4-1-1
URL: https://www.mot-art-museum.jp/
-------------
観光名称： 深川東京モダン館
住所： 東京都江東区門前仲町1-19-15
URL: http://fukagawatokyo.com/
-------------
観光名称： 東京都虹の下水道館
住所： 東京都江東区有明2-3-5
URL: https://www.nijinogesuidoukan.jp/
-------------
観光名称： 東京都立第五福竜丸展示館
住所： 東京都江東区夢の島2-1-1
URL: http://d5f.org/
-------------
観光名称： 東京都水の科学館
住所： 東京都江東区有明3-1-8
URL: http://www.mizunokagaku.jp/
-------------
観光名称： 東京臨海部広報展示室 TOKYO ミナトリエ
住所： 東京都江東区青海2-4-24
URL: http://www.tokyoport.or.jp/minatorie/index.html
-------------
観光名称： 東京ビッグサイト
住所： 東京都江東区有明3-10-1
URL: http://www.bigsight.jp/
-------------
観光名称： 水素情報館　東京スイソミル
住所： 東京都江東区潮見1-3-2
URL: https://www.tokyo-suisomiru.jp/
-------------
観光名称： そなエリア東京
住所： 東京都江東区有明3-8-35
URL: http://www.tokyorinkai-koen.jp/
```
code：
```python=
import openpyxl
wb=openpyxl.load_workbook("kotocity_tourism.xlsx",data_only=True)
ws=wb["kotocity_tourism"]

search=input("検索：")
print("\n結果：")
for row in ws:
    if search in row[4].value:
        print("-"*13)
        print("観光名称：",row[4].value)
        print("住所：",row[8].value)
        print("URL:",row[28].value)
```
