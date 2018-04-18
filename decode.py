import sys
import binascii

kewk = ""
for bulle in binascii.a2b_base64(sys.argv[1]):
    kewk += chr(ord(x)^95)
print kewk
