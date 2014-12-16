import csv
import numpy
from sklearn.neighbors import KDTree
from sklearn.externals import joblib
from array import array

if __name__ == "__main__":
        train_feat_path = 'train_feat_2'

        modu = 10
        train_lines = 40428967
        feats = 22
        
        train = [array('b', [0] * 136) for i in range(0, train_lines / modu + 1)]
        numpy.asarray(train)
        
        fin = open(train_feat_path, 'r')
        for i in range(0, train_lines):
            line = fin.readline()
            line = line.split()
            if i % modu == 0:
                for j in range(0,feats):
                    train[i/modu][int(line[j])] = 1 
            if (i+1) % 5000000 == 0:
                print('Finished ', i / 5000000)
        fin.close()

        print('-----')
        
        kdt = KDTree(train, leaf_size = 100, metric = 'euclidean')
        joblib.dump(kdt, 'model.pkl')

