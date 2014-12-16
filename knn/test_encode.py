import csv
import string
import sys

csvfile = open('../train/train.csv', 'r')
reader = csv.reader(csvfile)

item = 7
dic = {}

i = 0
for line in reader:
    i += 1
    if i > 1:
        x = line[item]
        y = line[1]
        if x+','+y in dic:
            dic[x+','+y] +=1
        else:
            dic[x+','+y] = 1
    if i % 5000000 == 0:
        print('Finished ', i / 5000000)
for key in dic.keys():
    print(key, dic[key])

exit
csvfile = open('../test/test.csv', 'r')
reader = csv.reader(csvfile)
predict = open('predict.csv', 'w', newline='')
writer = csv.writer(predict)

newdic = {}
i = 0
for line in reader:
    i += 1
    if i == 1:
        writer.writerow(['id', 'click'])
    if i > 1:
        x = line[item - 1]
        if x+',0' in dic:
            a = dic[x+',0']
        else:
            a = 0
        if x+',1' in dic:
            b = dic[x+',1']
        else:
            b = 0
        if (a + b > 10000):
            writer.writerow([line[0], b/(a+b)])
        else:
            writer.writerow([line[0], 0.17])            
predict.close()

#for key in newdic.keys():
#    print(key, newdic[key])


