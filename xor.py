from itertools import cycle, izip

def XOR(message, key):
     return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))