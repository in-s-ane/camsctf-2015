#!/usr/bin/python

import sys;

p = 2387138776635375741923867468329379132354280601643L
q = 2263287427372737185431258623661229697823729862967653333L

k = 5402781180552782668953973941046317096919389759822397332691011281833142607685445546514933124263094226119L
totient = 5402781180552782668953973941046317096919389759820134042876499768012335607137916848487730262045845971144L
c = 4616402371916851512416846198723321161968305983994265006483000709488116946220542876060407535554774112850L

# Assume ethan was right, in that cipher is indeed e, that makes k the mod
# So d is the modular inverse of c over k

def gcd(a,b): # Euclidean Algorithm
	while a:
		a, b = b%a, a;
	return b;

def egcd(a,b): # Extended Euclidean Algorithm
	if a == 0:
		return (b,0,1);
	else:
		g,y,x = egcd(b%a,a);
		return (g, x - (b // a) * y, y);

def modinv(a,m): # Modular Inverse Finder
	g, x, y = egcd(a,m);
	if g != 1:
		raise Exception('modular inverse does not exist');
	else:
		return x % m;

def printableAscii(string):
	charList = list(string);
	for el in string:
		if ord(el) < 32 or ord(el) > 126:
			return False;
	return True;

#d = modinv(c,totient); # Doesn't make sense b/c c is not coprime to totient
#d = modinv(c/2,totient); # Makes 0 sense

f = open("RSASolve.txt","a");

for e in range(int(sys.argv[1]),int(sys.argv[2])):
    try:
	if gcd(e,totient) == 1:
		d = modinv(e,totient);
		m = pow(c,d,k);
		hexM = hex(m);
		#print "e: %d" %(e);
		#print "d: %d" %(d);
		#print "Hex: %s" %(hex(d));
		if len(str(hexM)[2:-1]) % 2 == 0:
			#f.write("\n" + str(e) + ": " + str(hexM)[2:-1].decode("hex"));
			if printableAscii(str(hexM)[2:-1].decode("hex")):
				print str(hexM)[2:-1].decode('hex');
		#print "Result: %s" %(hex(d)[2:].decode("hex"));
    except KeyboardInterrupt:
        print e
        sys.exit(1)

print "we done here"


#Str = hexD[2:]
#print Str.decode("hex");
