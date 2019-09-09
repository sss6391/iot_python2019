from socket import *
from bluetooth import *
import time
 
server_ip = '192.168.0.5'
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((server_ip, port))
serverSock.listen(1)

client_socket1 = BluetoothSocket(RFCOMM)
client_socket2 = BluetoothSocket(RFCOMM)
client_socket1.connect(("B8:27:EB:E3:8B:7D",1))
client_socket2.connect(("B8:27:EB:73:28:0E",2))

# server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# server_socket.bind(("B8:27:EB:29:9A:57", 3))
# server_socket.listen(1)

# server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# port = 2
# server_socket.bind(("B8:27:EB:86:6E:39", port))
# server_socket.listen(1)

print('Server(%s) is waiting on %d port...' % (server_ip, port))
connectionSock, addr = serverSock.accept()
print(str(addr), ' connecting..')

while True:
    try:
        recvData = connectionSock.recv(1024).decode('utf-8')
        print('Receive Command : %s' % recvData)
        if recvData == '1':
            client_socket1.send('1')
        elif recvData == '2':
            client_socket1.send('2')
        elif recvData == '3':
            client_socket1.send('3')
        elif recvData == '4':
            client_socket1.send('4')
        elif recvData == '5':
            client_socket1.send('5')
        elif recvData == '6':
            client_socket1.send('6')

        if recvData == '21':
            client_socket1.send('7')
        elif recvData == '22':
            client_socket1.send('8')

        if recvData == '11':
            client_socket2.send('1')
        elif recvData == '12':
            client_socket2.send('2')
        if recvData == '14':
            client_socket2.send('4')
        elif recvData == '15':
            client_socket2.send('5')
        elif recvData == '16':
            client_socket2.send('6')

        if recvData == 'start':
            print(recvData)
            # a = '1'
            # serverSock.send('1'.encode('utf-8'))

        if recvData == 'q':
            client_socket1.send('q')
            client_socket2.send('q')
            time.sleep(1)
            connectionSock.close()
            break
        connectionSock.send('Receive OK'.encode('utf-8'))
    except Exception as e:
        print(e)
        
print('Server is shutdown')
