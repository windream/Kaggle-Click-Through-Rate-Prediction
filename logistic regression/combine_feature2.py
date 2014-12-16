__author__ = 'windream'

import math


def handle(input_folder, feat_sel, num_line, output_path):
    feat_file = {}
    for feat_name in feat_sel:
        feat_file[feat_name] = open(input_folder + feat_name, 'r')
    fout = open(output_path, 'w')

    row = []
    col = []
    data = []

    start_pos = {}
    num = 0
    for feat_name in feat_sel:
        start_pos[feat_name] = num
        num += int(feat_file[feat_name].readline())

    fout.write('%d\n' % num)
    for i in range(num_line):
        cnt = 0
        for feat_name in feat_sel:
            line = feat_file[feat_name].readline()
            #line = line.strip('\t\r\n')
            #fout.write(line)
            array = line.strip(' \t\r\n').split(':')
            ind = start_pos[feat_name] + int(array[0])
            val = int(array[1])
            cnt += 1
            #print(cnt)

            row.append(i)
            col.append(ind)
            data.append(val)
            '''if cnt < len(feat_sel):
                fout.write('%d:%d ' % (ind, val))
            else:
                fout.write('%d:%d' % (ind, val))
        fout.write('\n')'''

    print(max(row))
    print(len(row))
    for i in range(len(row)):
        #print(str(row[i]))
        fout.write(str(row[i]) + ' ')
    fout.write('\n')
    print(max(col))
    print(len(col))
    for i in range(len(col)):
        #print(str(col[i]))
        fout.write(str(col[i]) + ' ')
    fout.write('\n')

    for i in range(len(data)):
        #print(str(data[i]))
        fout.write(str(data[i]) + ' ')
    fout.write('\n')

    for feat_name in feat_sel:
        feat_file[feat_name].close()
    fout.close()


if __name__ == "__main__":
    # folder to store features
    feat_folder = '/Users/windream/Desktop/project/feature/'
    # path for combined train feature file
    train_feat_path = '/Users/windream/Desktop/project/trainCombine'
    # path for test feature file
    test_feat_path = '/Users/windream/Desktop/project/testCombine'
    # selected features
    #feat_sel = ['device_conn_type', 'device_type', 'app_category', 'site_category', 'banner_pos']
    feat_sel = ['hour', 'C1', 'banner_pos', 'site_id', 'site_domain', 'site_category', 'app_id' ,'app_domain', 'app_category', 'device_type', 'device_conn_type']
    # line number in train file
    num_line_train = 4042896#7#47686352
    # line number in test file
    num_line_test = 4577464#4769402

    if not feat_folder.endswith('/'):
        feat_folder += '/'

    print('train')
    handle(feat_folder + 'train/', feat_sel, num_line_train, train_feat_path)
    print('test')
    handle(feat_folder + 'test/', feat_sel, num_line_test, test_feat_path)
