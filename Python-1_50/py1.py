import re;
import base64
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))
    (r"([0-9a-f]+)",
        lambda m:p(m,y),
        base64.b64decode("NiA3CjExIGQgNiA0CjEgPSA0KDAsMWMpIAo1ID0gJzI9PScKMyA9IDMoIjE5JzFkIGMgMTggYSAxLiAxNyBlIDEwIDksIDE5JzE2IDEyIGUgMTQgNS4gZiBhIDE6ICIpCjFhIDE1KDMpID09IDE6Cgk4IDcuYig1KQoxMzoKCTggJzFiISc=")))
(lambda a,b:b[int("0x"+a.group(1),16)],"0|number|e24zdjNyX3VzZV9FVkFMfQ|input|randint|flag|import|base64|print|correctly|a|b64decode|thinking|random|you|Enter|guess|from|give|else|the|int|ll|If|of|I|if|Incorrect|10792579157912751097616189106168175192741851286517|m".split("|")))

'''
>>> "e24zdjNyX3VzZV9FVkFMfQ==".decode("base64")
'{n3v3r_use_EVAL}'

An alternate solution is to add the keyword 'not' after 'if' in the eval string
as such:
"0|number|e24zdjNyX3VzZV9FVkFMfQ|input|randint|flag|import|base64|print|correctly|a|b64decode|thinking|random|you|Enter|guess|from|give|else|the|int|ll|If|of|I|if not|Incorrect|10792579157912751097616189106168175192741851286517|m"

>> python py1.py
I'm thinking of a number. If you guess correctly, I'll give you the flag. Enter a number: 1
{n3v3r_use_EVAL}

'''
