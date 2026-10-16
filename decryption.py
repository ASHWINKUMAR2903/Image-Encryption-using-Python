import hashlib

def get_key_hash(key):
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % 256

try:
    path = input(r'Enter path of Image : ')
    
    key = input('Enter Key for decryption of Image (alphanumeric) : ')
    key = get_key_hash(key)
    
    print('The path of file : ', path)
    
    with open(path, 'rb') as fin:
        image = fin.read()
    
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    with open(path, 'wb') as fin:
        fin.write(image)
    
    print('Decryption Done...')

except Exception as e:
    print('Error caught:', str(e))