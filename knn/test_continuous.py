import csv
import string
import sys

csvfile = open('train_rev2.csv', 'r')
reader = csv.reader(csvfile)

item = 19
dic = [[0] * 2 for i in range(0,20000)]

i = 0
for line in reader:
    i += 1
    if i > 1:
        x = int(line[item])
        y = int(line[1])
        dic[x][y] += 1
    if i % 5000000 == 0:
        print('Finished ', i / 5000000)
#for key in dic.keys():
#    print(key, dic[key])

for i in range(0,20000):
    if (dic[i][0]+dic[i][1]>0):
        print(i, (dic[i][1]+0.18)/(dic[i][0]+dic[i][1]+1),dic[i][0],dic[i][1])

csvfile = open('test_rev2.csv', 'r')
reader = csv.reader(csvfile)
predict = open('predict.csv', 'w', newline='')
writer = csv.writer(predict)

i = 0
for line in reader:
    i += 1
    if i == 1:
        writer.writerow(['id', 'click'])
    if i > 1:
        x = int(line[item - 1])
        writer.writerow([line[0], (dic[x][1]+180)/(dic[x][0]+dic[x][1]+1000)])
predict.close()

#for key in newdic.keys():
#    print(key, newdic[key])


