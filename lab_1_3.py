#Read CSV file: https://docs.python.org/2/library/csv.html

import csv
import sys
import base64

csv.field_size_limit(10000000)
with open('crawl_data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		print('==> New Row:');
		j = 0;
		for col in row:
			print(str(j) + ':' + col)
			if j == 5:
				print('Decoded: ' + str(base64.b64decode(row[5])))
			elif j == 13:
				print('Decoded: ' + str(base64.b64decode(row[13])))
			elif j == 21:
				print('Decoded: ' + str(base64.b64decode(row[21])))
			j = j + 1;