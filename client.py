from socket import *
import time



serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.connect((serverName, serverPort))
numPings = 10
totalTime = 0
maxElapsed = 0
minElapsed = 0
numSuccess = 0

sentence = input('Input lowercase sentence:')

for i in range(numPings):
	
	start = time.time()
	clientSocket.send(sentence.encode())
	#now = time.time()
	#future = now + 5
	
	print('Ping #{}'.format(i))
	try:
		modifiedSentence = clientSocket.recv(1024)
		end = time.time()
		numSuccess += 1
		print('Message from server: ', modifiedSentence.decode())
		elapsed = end - start
		print('Elapsed time: {0:.6f}s\n'.format(elapsed))
		totalTime += elapsed
		if maxElapsed < elapsed:
			maxElapsed = elapsed
		if i == 1 or minElapsed > elapsed:
			minElapsed = elapsed
	except Exception:
		print('REQUEST TIMED OUT\n')
print('Max RTT time: {0:.6f}s'.format(maxElapsed))
print('Min RTT time: {0:.6f}s'.format(minElapsed))
print('Average RTT time: {0:.6f}s'.format(totalTime / numSuccess))
print('Packet loss: {0:.2f}%'.format(((numPings - numSuccess)/numPings)*100)) 
clientSocket.close()


