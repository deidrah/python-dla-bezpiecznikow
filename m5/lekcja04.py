from base64 import b64decode, b64encode

if __name__ == '__main__':
    data = 'Python jest fajny!'
    encoded = b64encode(data.encode())
    # print(f'{encoded=}')
    # print(type(encoded))
    encoded = encoded.decode()
    # print(f'{encoded=}')
    # print(type(encoded))
    

    decoded = b64decode(encoded)
    print(f'{decoded=}')
    decoded = decoded.decode()
    print(f'{decoded=}')

    with open('random.bin', 'rb') as infile:
        data = infile.read()

    encoded = b64encode(data)
    print(f'{encoded=}')