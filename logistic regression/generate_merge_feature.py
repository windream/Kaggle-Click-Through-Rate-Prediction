import csv
import string
import sys

csvfile = open('../train/train.csv', 'r')
reader = csv.reader(csvfile)

feats = 22
dic = [ dict() for i in range(0, feats)]
merge = [ dict() for i in range(0, feats)]

i = 0
for line in reader:
    i += 1
    if i > 1:
        for j in range(2, feats+2):
            x = line[j]
            if j == 2:
                x = x[6] + x[7]
            if x in dic[j-2]:
                dic[j-2][x] +=1
            else:
                dic[j-2][x] = 1
    if i % 5000000 == 0:
        print('Finished ', i / 5000000)

csvfile.close()

threshold = 100000
tot = 0
st = []
for j in range(0,feats):
    st.append(tot)
    for x in dic[j]:
        if dic[j][x] >= threshold:
            tot += 1
            merge[j][x] = tot
        else:
            merge[j][x] = st[j]
    tot += 1

print(tot)

csvfile = open('../train/train.csv', 'r')
reader = csv.reader(csvfile)
train_feat = open('train_feat_0', 'w')
train_feat_lib = open('train_feat_lib_0', 'w')

i = 0
for line in reader:
    i += 1
    if i > 1:
        train_feat_lib.write('%d' % (int(line[1])))
        for j in range(2, feats+2):
            x = line[j]
            if j == 2:
                x = x[6] + x[7]
            if x in dic[j-2]:
                train_feat.write('%d ' % (merge[j-2][x]))
                train_feat_lib.write(' %d:1' % (merge[j-2][x]))
            else:
                train_feat.write('%d ' % (st[j-2]))
                train_feat_lib.write(' %d:1' % (st[j-2]))
        train_feat.write('\n')
        train_feat_lib.write('\n')

csvfile.close()
train_feat.close()
train_feat_lib.close()

csvfile = open('../test/test.csv', 'r')
reader = csv.reader(csvfile)
test_feat = open('test_feat_0', 'w')
test_feat_lib = open('test_feat_lib_0', 'w')

i = 0
for line in reader:
    i += 1
    if i > 1:
        test_feat_lib.write('%d' % (0))
        for j in range(1, feats+1):
            x = line[j]
            if j == 1:
                x = x[6] + x[7]
            if x in dic[j-1]:
                test_feat.write('%d ' % (merge[j-1][x]))
                test_feat_lib.write(' %d:1' % (merge[j-1][x]))
            else:
                test_feat.write('%d ' % (st[j-1]))
                test_feat_lib.write(' %d:1' % (st[j-1]))
        test_feat.write('\n')
        test_feat_lib.write('\n')                

csvfile.close()
test_feat.close()
test_feat_lib.close()

#for key in newdic.keys():
#    print(key, newdic[key])


