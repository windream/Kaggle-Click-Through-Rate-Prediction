import csv
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib
from array import array

if __name__ == "__main__":
        test_feat_path = 'test_feat_2'
        modu = 10
        train_lines = 40428967
        test_lines = 4577464
        feats = 22
        firstk = 100

        test = [0] * 136
        cur = [0] * firstk
        label = [0] * (train_lines / modu + 1)
        ans = [0] * test_lines

        fin = open('../train/label', 'r')
        for i in range(0, train_lines):
            if i % modu == 0:
                label[i/modu] = int(line)    
            if (i+1) % 5000000 == 0:
                print('Finished ', i / 5000000)
        fin.close()        

        kdt = joblib.load('model.pkl')
        fin = open(test_feat_path, 'r')
        for i in range(0, test_lines):
            test = [0] * 136
            line = fin.readline()
            line = line.split()
            for j in range(0, feats):
                test[int(line[j])] = 1 
            cur = kdt.query(test, firstk, return_distance = False)
            for j in range(0, firstk):
                if (label[cur[j]] == 1):
                    ans[i] += 1
            ans[i] = 1.0 * (ans[i] + 1) / (firstk + 1)        
            if (i+1) % 5000000 == 0:
                print('Finished ', i / 5000000)
        fin.close()

        print('-----')
        
        csvfile = open('../test/test.csv', 'r')
        reader = csv.reader(csvfile)
        predict = open('predict.csv', 'w')
        writer = csv.writer(predict)

        i = 0
        for line in reader:
            if i == 0:
                writer.writerow(['id', 'click'])
            if i > 0:
                writer.writerow([line[0], ans[i-1]])
            i += 1
        csvfile.close()
        writer.close()
