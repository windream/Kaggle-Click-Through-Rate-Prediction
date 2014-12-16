import random

if __name__ == "__main__":
	# source file
	source_file = "../feature/train.feat"
	# train file
	target_file = "../feature/train_sample.feat"
	# percentage
	ratio = 0.2

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

	target_set = set(random.sample(range(1, num_line + 1), int(num_line * ratio)))

	fin = open(source_file, 'r')
	fout = open(target_file, 'w')
	p = 0
	first_line = True
	for line in fin:
		if first_line:
			first_line = False
			fout.write(line)
			continue
		p += 1
		if p in target_set:
			fout.write(line)
	fin.close()
	fout.close()