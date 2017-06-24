#Read CSV file: https://docs.python.org/2/library/csv.html

import csv

csv.field_size_limit(10000000)
with open('crawl_data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		print('==> New Row:');
		j = 0;
		for col in row:
			print(str(j) + ':' + col)
			j = j + 1;