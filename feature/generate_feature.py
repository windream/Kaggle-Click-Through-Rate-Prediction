import math
import os
import sys

def process_line(line, dic, feat_index):
	array = line.strip(' \t\r\n').split(',')
	for feat_name in feat_index.keys():
		c = array[feat_index[feat_name]]
		if feat_name == 'hour':
			c = c[-2:]
		if not dic[feat_name].has_key(c):
			k = len(dic[feat_name])
			dic[feat_name][c] = k

def output_feat_line(line, dic, feat_index, feat_file):
	array = line.strip(' \t\r\n').split(',')
	for feat_name in feat_index.keys():
		c = array[feat_index[feat_name]]
		if feat_name == 'hour':
			c = c[-2:]
		feat_file[feat_name].write('%d:1\n' % dic[feat_name][c])

if __name__ == "__main__":
	# path of train file
	train_file = '../data/train_sampled_80'
	# path of validation file
	val_file = '../data/val_sampled_80'
	# path of test file
	test_file = '../data/test'
	# path of the folder to store feature
	feat_folder = '../feature/80_percent_val'
	
	if not feat_folder.endswith('/'):
		feat_folder += '/';

	if not os.path.exists(feat_folder + 'train/'):
		os.mkdir(feat_folder + 'train/')
	if not os.path.exists(feat_folder + 'val/'):
		os.mkdir(feat_folder + 'val/')
	if not os.path.exists(feat_folder + 'test/'):
		os.mkdir(feat_folder + 'test/')

	# feature index for each line, starting from 0
	train_feat_index = {'hour': 2, 'C1': 3, 'banner_pos': 4, 'site_id': 5, 'site_domain': 6, 'site_category': 7, 'app_id': 8, 'app_domain': 9, 'app_category': 10, 'device_id': 11, 'device_ip': 12, 'device_model': 13, 'device_type': 14, 'device_conn_type': 15, 'C14': 16, 'C15': 17, 'C16': 18, 'C17': 19, 'C18': 20, 'C19': 21, 'C20': 22, 'C21': 23}
	val_feat_index = {'hour': 2, 'C1': 3, 'banner_pos': 4, 'site_id': 5, 'site_domain': 6, 'site_category': 7, 'app_id': 8, 'app_domain': 9, 'app_category': 10, 'device_id': 11, 'device_ip': 12, 'device_model': 13, 'device_type': 14, 'device_conn_type': 15, 'C14': 16, 'C15': 17, 'C16': 18, 'C17': 19, 'C18': 20, 'C19': 21, 'C20': 22, 'C21': 23}
	test_feat_index = {'hour': 1, 'C1': 2, 'banner_pos': 3, 'site_id': 4, 'site_domain': 5, 'site_category': 6, 'app_id': 7, 'app_domain': 8, 'app_category': 9, 'device_id': 10, 'device_ip': 11, 'device_model': 12, 'device_type': 13, 'device_conn_type': 14, 'C14': 15, 'C15': 16, 'C16': 17, 'C17': 18, 'C18': 19, 'C19': 20, 'C20': 21, 'C21': 22}
	
	dic = {}
	for feat_name in train_feat_index.keys():
		dic[feat_name] = {}

	#
	# build index table for each feature
	#
	fin = open(train_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False	
		else:
			process_line(line, dic, train_feat_index)
	fin.close()

	fin = open(val_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			process_line(line, dic, val_feat_index)
	fin.close()

	fin = open(test_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			process_line(line, dic, test_feat_index)
	fin.close()

	#
	# obtain train feature
	# 
	train_feat_file = {}
	for feat_name in train_feat_index.keys():
		train_feat_file[feat_name] = open(feat_folder + 'train/' + feat_name, 'w')
		train_feat_file[feat_name].write('%d\n' % len(dic[feat_name]))
	fin = open(train_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			output_feat_line(line, dic, train_feat_index, train_feat_file)
	fin.close()
	for feat_name in train_feat_index.keys():
		train_feat_file[feat_name].close()

	#
	# obtain val feature
	# 
	val_feat_file = {}
	for feat_name in val_feat_index.keys():
		val_feat_file[feat_name] = open(feat_folder + 'val/' + feat_name, 'w')
		val_feat_file[feat_name].write('%d\n' % len(dic[feat_name]))
	fin = open(val_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			output_feat_line(line, dic, val_feat_index, val_feat_file)
	fin.close()
	for feat_name in val_feat_index.keys():
		val_feat_file[feat_name].close()

	#
	# obtain test feature
	# 
	test_feat_file = {}
	for feat_name in test_feat_index.keys():
		test_feat_file[feat_name] = open(feat_folder + 'test/' + feat_name, 'w')
		test_feat_file[feat_name].write('%d\n' % len(dic[feat_name]))
	fin = open(test_file, 'r')
	first_line = True	
	for line in fin:
		if first_line:
			first_line = False
		else:
			output_feat_line(line, dic, test_feat_index, test_feat_file)
	fin.close()
	for feat_name in test_feat_index.keys():
		test_feat_file[feat_name].close()

	#
	# obtain train label
	#
	fout = open(feat_folder + 'train/' + 'label', 'w')
	fin = open(train_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			array = line.strip(' \t\r\n').split(',')
			fout.write('%s\n' % array[1])
	fin.close()
	fout.close()

	#
	# obtain val label
	#
	fout = open(feat_folder + 'val/' + 'label', 'w')
	fin = open(val_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			array = line.strip(' \t\r\n').split(',')
			fout.write('%s\n' % array[1])
	fin.close()
	fout.close()

	#
	# obtain test label
	#
	fout = open(feat_folder + 'test/' + 'label', 'w')
	fin = open(test_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
		else:
			array = line.strip(' \t\r\n').split(',')
			fout.write('0\n')
	fin.close()
	fout.close()