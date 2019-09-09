from socket import *

port = 8080
server_ip = '192.168.0.5'
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, port))

print("Connecting to the server(%s) on %d port" %(server_ip, port))

while True:
    sendData = input('>>> ')
    clientSock.send(sendData.encode('utf-8'))
    recvData = clientSock.recv(1024).decode('utf-8')
    print('서버: ', recvData)

clientSock.close()
print('Client is shutdown')

