from bluetooth import *
import pygame
import time
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("00:18:E5:04:11:8E", 1))
while True:
    msg = raw_input("Send : ")
    print(msg)
    if msg == 'open':
        print('oooooooo')
        pygame.mixer.init()
        pygame.mixer.music.load("a.wav")
        pygame.mixer.music.play()
        client_socket.send('1')
        time.sleep(5)
        pygame.mixer.music.close()

    if 'close' == msg:
        pygame.mixer.init()
        pygame.mixer.music.load("a.wav")
        pygame.mixer.music.play()
        client_socket.send('2')
        time.sleep(5)

    if msg[0] == 'q':
        break
    client_socket.send(msg)



print("Finished")
client_socket.close()


