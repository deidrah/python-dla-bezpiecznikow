import socket


ports = [53, 80, 443, 444]
i = 0
# print(ports[i])``
# print(len(ports))
while i < len(ports):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(1)

    ip = '8.8.8.8'
    port = ports[i]
    address = (ip, port)

    result = mysocket.connect_ex(address)

    if result == 0:
        print('port', port, 'jest otwarty')
    else:
        print('port', port, 'jest zamknięty')

    mysocket.close()
    # i = i + 1
    i += 1