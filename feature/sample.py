import random

if __name__ == "__main__":
	# source file
	source_file = "../data/train"
	# train file
	train_file = "../data/train_sampled_80"
	# validation file
	val_file = "../data/val_sampled_80"
	# ratio of sampled lines
	ratio = 0.8

	# line number
	num_line = 0

	fin = open(source_file, 'r')
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
			continue
		num_line += 1
	fin.close()

	train_set = set(random.sample(range(1, num_line + 1), int(num_line * ratio)))
	#temp = set(range(1, num_line + 1)) - train_set
	#val_set = set(random.sample(temp, int(num_line * ratio)))
	val_set = set(range(1, num_line + 1)) - train_set

	fin = open(source_file, 'r')
	fout1 = open(train_file, 'w')
	fout2 = open(val_file, 'w')
	p = 0
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
			fout1.write(line)
			fout2.write(line)
			continue
		p += 1
		if p in train_set:
			fout1.write(line)
		elif p in val_set:
			fout2.write(line)
	fin.close()
	fout1.close()
	fout2.close()