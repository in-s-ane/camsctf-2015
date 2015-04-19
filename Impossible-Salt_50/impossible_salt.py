#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, random

def salt_filename(filename):
	return hashlib.sha512((generate_salt() + filename).encode()).hexdigest()[:50]
	
def generate_salt():
	SALT = 'saltystuff'
	for i in range(0, 10000):
		S4LT = SALT + str(random.randint(0, 9))
		
	return hashlib.sha512(S4LT.encode()).hexdigest()

print generate_salt()
print salt_filename('flag.txt')
