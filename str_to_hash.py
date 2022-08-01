import hashlib
s = "Python Bootcamp"
hash_object = hashlib.sha256(b'${s}')
hex_dig = hash_object.hexdigest()
print(hex_dig)
