# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

#put encrypted byte string here:
encrypted = b'rXx/R/KoaUrVlpMLkzMQM/R1MNt3x41NRZcFnUnBxkwC+4L00QEIcT5j+yA0KCXU7lyrboqdkU31yvj6d5dNAx4qeNlI4lh96NdvdPWkVMmdUU24J2/SwTW48Jh+rQr2STu2um2MImEtJw9+RGu+vevIZOaQdtIDuECv7V7Ar3VL57XKkne4JOLzxA72/YgALEEKkJy1LDzXXOkSD1hlW55hZitxfYglq5Re8hVxJoljE30B5GrwqZtG7uVxNgo0TFRYKQ1zSyph94kRqpSCK4y24qk6sHTKUEFnY+2jYfaMnkJXzdkUgIznR+mJFKe3vXxoB4dUuR3EgvJRyNczVQ=='

#retrieve the private key from the .pem and use it here
#
#

original_message = private_key.decrypt(
    base64.b64decode(encrypted),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)