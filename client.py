from socket import *
import time

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)

clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode())
#now = time.time()
#future = now + 5

modifiedSentence = clientSocket.recv(1024)

print('From Server:', modifiedSentence.decode())

clientSocket.close()

