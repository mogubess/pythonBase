
from sqlalchemy import values


print('I don\'nt now')

# 先頭にrを付けてrawデータとするか
print(r'c:\name\name')
# バックスラッシュをつけて
print('c:\\name\\name')

# ダブル久オート３つで改行を入れる
print("""
line1
line2
line3
""")

print('Hi' * 3)

print('Py' + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaa'
    'bbbbbbbbbbbbbbbbbbbbbb')

print(s)

word = 'python'

#先頭文字
print(word[0])
#終端文字
print(word[-1])
#index0(最初)からindex2までの文字
print(word[0:2])
print(word[:2])
#ho
print(word[3:-1])
#2番目から最後まで thon
print(word[2:])

#文字列はイミュターブルのためException発生
try:
    word[0] ='j'  # exception
except TypeError as e:
    print(e) # 'str' object does not support item assignment

#新たに文字列を作成する（word変数への上書き）
word = 'j' + word[1:]
print(word)

#全配列の選択
print(word[:])

#文字列の長さ
print(len(word))

#===========================================================
#文字列のメソッド
#===========================================================
print('################################################')
s = 'eMy name is Mike. Hi y Mike'

#先頭の文字列が'My'から始まっているからを判定
is_start = s.startswith('My')
print(is_start)

#最初の文字を大文字にして残りを小文字
print(s.capitalize())
#文節ごとの文字を大文字にする
print(s.title())
#すべての文字を大文字にすすｒ
print(s.upper())
#小文字
print(s.lower())

ss ='abc-xyz-123-789-ABC-XYZ'

import re
#正規表現一致()
#\d 1文字以上の数字
print(re.sub('\d+','FFF',ss))

#最初から検索、見つかった箇所の先頭Index(11)
print(s.find('Mike'))

#最後から検索、見つかった箇所先頭Index(20)
print(s.rfind('Mike'))

#検索個数(2)
print(s.count('Mike'))

#文字列置き換え
print(s.replace('Mike', 'Nacy'))

#reprは表示文字列をシングル久御テーションんで囲む
print(repr(s))
#引数がない場合は、先頭のスペース、改行、全角スペースをなくす
print(s.strip())

#引数は、削除したい文字の組み合わせを指定します
#先頭/末尾から引数charsに含まれない文字に達するまで文字が削除されます
#返り値は、先頭/末尾から文字を削除したコピーを返します
print(s.strip('e'))

#先頭から
print(s.lstrip('e'))

#末尾から
print(s.rstrip('e'))

#文字列の左右寄席、真ん中よせ
sss ='abc'
print(sss.center(8))
print(sss.center(8,'+'))

print(sss.rjust(8,'-'))

print(sss.ljust(8,'*'))

#0で埋めて右寄せ、+/-を考慮する
print('-123'.zfill(8))

n=456
print(str(n).center(8,'@'))

#format
print('right : {:@>8}'.format(sss))
# right : @@@@@abc

print('center: {:@^8}'.format(sss))
# center: @@abc@@@

print('left  : {:@<8}'.format(sss))
# left  : abc@@@@@

n = 255

print('right : {:08}'.format(n))
# right : 00000255

print('right : {:08x}'.format(n))
# right : 000000ff


#文字列をバイト列の変換
ccah = 'あいうえお'
ccaa = 'Heloo every body'
print(ccah.encode('utf-8'))
print(ccaa.encode('utf-8'))
bccah= ccah.encode('utf-8')
print('{:x}'.format(bccah[0]))

#桁合わせ表記
#print('{:08x}'.format(bccah[0]))

bccaa= ccaa.encode('utf-8')
print(bccah.decode('utf-8'))
print(bccaa.decode('utf-8'))


aaa = 'first'
bbb = aaa #コピー
aaa = 'second'
print(f'{aaa} : {bbb}')