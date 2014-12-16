import random

if __name__ == '__main__':
	# source file
	source_file = '../data/train_sampled_10'
	# target file
	target_file = '../data/train_sampled_10_shuffled'

	fin = open(source_file, 'r')
	fout = open(target_file, 'w')

	line = fin.readline()
	fout.write(line)

	lines = fin.readlines()
	random.shuffle(lines)
	fout.writelines(lines)

