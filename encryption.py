import hashlib

def get_key_hash(key):
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % 256
    #1.Convert the password string into UTF-8 bytes using key.encode(). For example, "123" becomes decimal byte values [49, 50, 51], like ascii.
    #2.Calculate the SHA-256 hash of those bytes, producing a 256-bit (32-byte) raw hash.
    #3.Convert the 32-byte hash into 64 hexadecimal characters using .hexdigest().
    #4.Convert the 64-character hexadecimal string into a base-10 integer using int(hash_hex, 16).
    #5.Calculate the remainder after dividing the integer by 256 using % 256, producing a value between 0 and 255 (an 8-bit XOR key).

try:
    path = input(r'Enter path of Image : ')
    
    key = input('Enter Key for encryption of Image (alphanumeric) : ')
    key = get_key_hash(key)
    
    print('The path of file : ', path)
    print('Key for encryption : ', key)
    
    with open(path, 'rb') as fin:
        image = fin.read()
    
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    with open(path, 'wb') as fin:
        fin.write(image)
    
    print('Encryption Done...')

except Exception as e:
    print('Error caught:', str(e))
