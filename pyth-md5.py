import hashlib
import sys

def decoder(pin):
    res_hash=hashlib.md5(pin.encode())
    temp_hash=res_hash.hexdigest()
    return temp_hash

args=str(sys.argv[1])
print(args)

pin="0000"
temp=decoder(pin)
if temp==args:
    print("PIN : ",pin)

i=999;
while (i<10000):
    pin=str(i)
    temp_hash=decoder(pin)
    if temp_hash==args:
        print("PIN :",i)
    i=i+1
