count = 0
while count <= 5:
    if count >= 3:
        break

    if count == 2:
        count +=1
        continue

    print(count)
    count += 1
else:
    #for文も同じ
    #breakなどで抜けなければ通る
    print('done!')