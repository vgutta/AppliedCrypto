from Crypto.Util.number import *
import hashlib

#PYTHON 2...

def generate_seed(secret, nonce):
    return bytes_to_long(hashlib.sha256(nonce + secret).digest()) % 2**32

def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)

def generate_byte_array(seed, num_bytes):
  generator = crand(seed)
  return [generator.next() % 256 for _ in range(num_bytes)]
