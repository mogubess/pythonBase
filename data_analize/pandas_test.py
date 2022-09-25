import numpy as np
import pandas as pd

#1次元配列作成
s = pd.Series([1,2,np.nan])
print(s)
print(s[0])
#各種演算
print(s.sum())

#2次元の配列ラベルつき
df = pd.DataFrame({'A':[1,2], 'B':[3,4]})
print(df)
print(df.dtypes)

#縦６横４の2次元配列
#INDEXとラベルを入れる
df = pd.DataFrame(np.random.randn(6,4), index=pd.date_range('20170101',periods=6),columns=['A','B','C','D'])
print(df)

print(df.head(1))
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)

print(df.sort_values(by='B'))

print(df[0:3])
#指定範囲のリストを返す
print(df['20170102':'20170104'])
#指定インデックスの行を返す
print(df.loc['20170101'])

#指定インデックスの行を返す(列指定)
print(df.loc['20170101',['B']])

#Bの列だけ取得
print(df.loc[:,['B']])

#(0,0)の値取得
print(df.iloc[0,0])

#0-2/0-2の範囲を取得
print(df.iloc[0:2,0:2])

#Bの列で0以上のもの
print(df[df.B > 0])

#0より大きいものを出力
print(df[df > 0])

df2 = df.copy()
df2['E'] = ['one','one','two','three','four','three']
print(df2)

#E列からマッチングするものを取り出す
print(df2[df2['E'].isin(['one','four'])])

#E列の追加
ss = pd.Series([1,2,3,4,5,6], index=pd.date_range('20170101',periods=6))
print(ss)

df['E'] = ss
print(df)
#行を1段下げる
print(df.shift(1))

#行列の結合(縦方向)
df = pd.DataFrame(np.random.randn(2,2))
print(pd.concat([df,df]))

#作成した列の1行目を一番したの行につける
df = pd.DataFrame(np.random.rand(8,4),columns=['A','B','C','D'])
print(df)
#一行目取り出す
s = df.iloc[0]

#一番下に結合するためのデータを作成
df_append = pd.DataFrame([s.values.tolist()], columns=df.columns)

print(df_append)
print(pd.concat([df,df_append],ignore_index=True))


#同じグループまとめて計算
df = pd.DataFrame({'A':['foo','bar','foo','bar'], 'B':np.random.randn(4)})
print(df)

print(df.groupby('A').sum())

import pandas_datareader
df = pandas_datareader.data.DataReader('AAPL','yahoo','2014-01-01')
print(df.head(1))
