# Cryptographic Hash Function and Algorithm
# SHA-256    py

import hashlib

string = input("Enter Text for hashing: ") 

# Hash that favourite quote...

encoded = string.encode()
result = hashlib.sha256(encoded)
hexa = result.hexdigest()
print("String:\n", string, "\n", end="")
print("Hash value:\n", result, "\n", end="")
print("Hexadecimal equivalent:\n", hexa, "\n",)

print("Digest size: ", result.digest_size, "\n", end="")
print("Block Size:", result.block_size, "\n", end="")

# Twilight Times...

# Ink✌
