import collections

d = {}
l = ['a','a','a','b','b','c']
for word in l:
    if word not in d:
        d[word]=0
    d[word]+=1
print(d)

d = {}
l = ['a','a','a','b','b','c']
for word in l:
    d.setdefault(word,0)
    d[word] +=1
print(d)

d=collections.defaultdict(int)
l = ['a','a','a','b','b','c']
for word in l:
    d[word] +=1
print(d)

#各文字をKeyとして数をvalueとして、辞書を作成する
l = ['a','a','a','b','b','c']
c = collections.Counter()
for word in l:
    c[word] +=1
print(c)
print(c.most_common(2))   #もっとも多い組み合わせから順に２つまで返す
print(sum(c.values()))    #6  文字列の総数を数える

import re

# 任意のファイルから、文字列単位（r'\w+(）)で取り出し、一番多い文字列をカウントする
# with open('collections_Counter.py','r') as f:
#     words = re.findall(r'\w+', f.read().lower())
#     print(collections.Counter(words).most_common(20))
