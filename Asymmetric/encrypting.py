# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import binascii

message = b'put your message here!'

#retrieve the public key and use it here
#
# public_key = 
#
#

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#prints byte string
print(encrypted)

#prints ascii string
#encryptedString = binascii.hexlify(encrypted).decode('ascii')
#print(encryptedString)