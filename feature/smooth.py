import sys
import math

if __name__ == "__main__":
	source_file = '../result/result_31'
	target_file = '../result/result_50'
	threshold = 0.01

	fin = open(source_file, 'r')
	fout = open(target_file, 'w')

	for line in fin:
		value = float(line.strip(' \t\r\n'))
		if value < threshold:
			value = 0.01
		elif value > 1 - threshold:
			value = 1 - threshold
		fout.write('%f\n' % value)

	fin.close()
	fout.close()