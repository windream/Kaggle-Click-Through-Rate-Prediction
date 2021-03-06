import math

def handle(input_folder, feat_sel, num_line, output_path):
	fin = open(input_folder + 'label', 'r')
	feat_file = {}
	for feat_name in feat_sel:
		feat_file[feat_name] = open(input_folder + feat_name, 'r')
	fout = open(output_path, 'w')

	start_pos = {}
	num = 0
	for feat_name in feat_sel:
		start_pos[feat_name] = num
		num += int(feat_file[feat_name].readline())

	for i in range(num_line):
		fout.write(fin.readline().strip(' \t\r\n'))
		for feat_name in feat_sel:
			line = feat_file[feat_name].readline()
			array = line.strip(' \t\r\n').split(':')
			ind = start_pos[feat_name] + int(array[0])
			val = array[1]
			fout.write(' %d:%s' % (ind, val))
		fout.write('\n')

	fin.close()
	for feat_name in feat_sel:
		feat_file[feat_name].close()
	fout.close()	


if __name__ == "__main__":
	# folder of features
	feat_folder = 'feature/'
	# path for combined train feature file
	train_feat_path = 'train.feat'
	# path for test feature file
	test_feat_path = 'test.feat'
	# selected features
	feat_sel = ['hour', 'C1', 'banner_pos', 'site_id', 'site_domain', 'site_category', 'app_id' ,'app_domain', 'app_category', 'device_type', 'device_conn_type']
	
	# line number in train file
	num_line_train = 0
	# line number in test file
	num_line_test = 0

	if not feat_folder.endswith('/'):
		feat_folder += '/';

	fin = open(feat_folder + 'train/label', 'r')
	for line in fin:
		num_line_train += 1
	fin.close()

	fin = open(feat_folder + 'test/label', 'r')
	for line in fin:
		num_line_test += 1
	fin.close()

	handle(feat_folder + 'train/', feat_sel, num_line_train, train_feat_path)
	handle(feat_folder + 'test/', feat_sel, num_line_test, test_feat_path)