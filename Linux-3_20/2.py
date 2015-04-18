import random

import os

for i in range(1000):

	f = open(str(i) + '.txt', 'w')

	f.close()

for filename in os.listdir('/home/cs/Desktop/2'):

	if filename == '742.txt':

		f = open(filename, 'r+')

		f.write('{l00king_4rouNd_3H?}')

		f.close()

	else:

		f = open(filename, 'r+')

		f.write(str(random.randint(0,25891895192051795)))
