"""
#使わないけど頑張って書いたので残します。
def fixexcel(df):
    #関数を使用して、要らない列を削除する。
    try:
        #行の場合　axis=0 列の場合　axis=1
        #若找不到則跳出ERROR
        df=df.drop(["メールアドレス"],axis=1)
        print(df)
        #二行目までのデータは要らないので除去。　
        df=df.iloc[2:]
        return df
    except:
        print("編集する必要ない")
        #編集しなくていい場合でもreturn
        return df
"""
"""
    try:
        #locで行のデータ取得する。ない場合エラーになるので例外処理。
        df=df.loc[name]
        return df
    except:
        print("見つかりません")
"""

import os
import pandas as pd
import glob

#入力した名前が行の先頭にあるかどうか。
def checkdf(df,name):
    #もしあったら、データを抽出。
    if name in df.index:
        #指定した行のデータを取得する。
        df=df.loc[name]
        return df,name
    else:
        print("そんな人いない。")
        return df,False

#生徒1人のテストデータを取得。
def getOneStudent(df):
    while True:
        name=input("スペース区切りで名前を入力してください：")
        df,name=checkdf(df, name)
        if name==False:
            continue
        else:
            return df,name
    
#生徒一人のテスト結果を表示する。
def showOneStudent(df):
    studentState,name=getOneStudent(df)
    if name== False:
        print("そんな人いません")
    else:
        print(studentState)

#取得したデータをexcelにする
def outputdata(df,name):
    df=pd.DataFrame(df)
    #条件でテスト済んでいない人を選別する
    df=df[df[name] == "-"]
    #終わったら長さ0より大きいやつ、excelファイルとして出力する。
    len(df.index)>0 and df.to_excel(foldername+"\\L2"+name+".xlsx")

#生徒1人、テスト済んでいないデータを取得。
def onelosttest(df,name=True):
    if name==True:
        #普通に呼び出すと、getOneStudentで入力して必要なデータを選別する。
        df,name = getOneStudent(df)
        #選別終わったら出す。
        outputdata(df,name)
        print("処理が終わりました")
    else:
        #名前がある場合は直接選別行う。
        df,name=checkdf(df,name)
        #出す。
        outputdata(df,name)

#すべて生徒、テスト済んでいないデータを取得。
def alllosttest(df):
    #全員のデータが必要な場合は要は一人分を全人分にするだけなので、for使って名前全部入れる。
    for i in df.index:
        onelosttest(df,i)
    print("処理が終わりました")
    

#FUNTIONを全部ここに入れました。
fun_dict={"1":showOneStudent,
          "2":onelosttest,
          "3":alllosttest}

#ファイル内のexcelを全て取得する。
file=glob.glob("*.xlsx")
#ファイルごとに処理を行っていく。
for i in file:
    print("今操作しているのは"+i)
    #フォルダーを作成する前にフォルダー名を作成する。
    foldername=i.replace(".xlsx", "")
    #フォルダーを作る。
    os.makedirs(foldername,exist_ok=True)
    #excelを読み取り、index_colではじめの列を決める。
    df=pd.read_excel(i,index_col=(1))
    
    while True:
        print("1:生徒一人のテスト結果を取得　2:生徒一人未完了テストを取得 3:全ての生徒の未完成テストのデータを取得 4:end")
        num=input()
        if num=="4":
            break
        elif num not in fun_dict.keys():
            print("無効")
            continue
        else:
            fun_dict[num](df)
