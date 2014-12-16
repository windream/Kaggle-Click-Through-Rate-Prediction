import math
import sys

if __name__ == "__main__":
	fin1 = open('result_31', 'r')
	fin2 = open('result_42', 'r')
	fout = open('../result/result_55', 'w')
	for line in fin1:
		x = float(line.strip(' \r\n\t'))
		y = float(fin2.readline().strip(' \r\n\t'))
		fout.write('%f\n' % (0.55 * x + 0.45 * y))
	fin1.close()
	fin2.close()
	fout.close()
