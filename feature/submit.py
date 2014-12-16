import sys
import os
import math

if __name__ == '__main__':
	# prediction file
	pred_file = '../result/result_55'
	# test file
	sample_file = '../submission/sampleSubmission'
	# target file
	target_file = '../submission/submission_55'

	fin1 = open(pred_file, 'r')
	fin2 = open(sample_file, 'r')
	fout = open(target_file, 'w')

	fout.write(fin2.readline())
	for line in fin1:
		x = fin2.readline().strip(' \t\r\n').split(',')[0]
		y = line.strip(' \t\r\n')
		fout.write("%s,%s\n" % (x, y))

	fin1.close()
	fin2.close()
	fout.close()
