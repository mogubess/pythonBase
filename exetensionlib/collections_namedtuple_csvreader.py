import collections
import csv

#csvの書き込みは空行がはいるので、newline=""とすること
with open('named.csv', 'w', newline='') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first':'Mike','last':'Jackson','address': 'A'})
    writer.writerow({'first':'Jun','last':'Sakai','address': 'B'})
    writer.writerow({'first':'Nancy','last':'Mask','address': 'C'})

with open('named.csv','r') as f:
    csv_reader = csv.reader(f)
    # next(csv_reader),csv_readerからデータ取得後にイテレータを進める
    # Names = collections.namedtuple('Names', ['first', 'last', 'address'])
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        # 1.names = Names._make(['Mike', 'Jackson', 'A'])
        # 2.names = Names._make(['Jun', 'Sakai', 'B'])
        # 3.names = Names._make(['Nancy', 'Mask', 'C'])
        names = Names._make(row)
        print(names.first, names.last, names.address)