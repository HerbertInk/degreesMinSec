# Hash the Valentine
# Feb 14 2022

import hashlib

# string = "Feb142022"
string = input("Your Valentine: ")
encoded = string.encode()
result = hashlib.sha256(encoded)

print("String: ", string, "\n", end="")
print("Hash value: ", result, "\n", end="")
print("Hexadecimal: ", result.hexdigest())

print("Digest size: ", result.digest_size, "\n", end="")
print("Block Size:", result.block_size, end="")

# Ink
