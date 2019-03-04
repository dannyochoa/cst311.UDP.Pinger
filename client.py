from socket import *
import time

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.connect((serverName, serverPort))
numPings = 10
#amount of time it takes to send the 10 packets 
totalTime = 0
#longest round trip time
maxElapsed = 0
#shortest round trip time
minElapsed = 0
numSuccess = 0

sentence = input('Input lowercase sentence:')

for i in range(numPings):
	
	start = time.time()
	clientSocket.send(sentence.encode())
	
	print('Ping #{} time: {}'.format(i+1, start))
	try:
		modifiedSentence = clientSocket.recv(1024)
		end = time.time()
		numSuccess += 1
		print('Message from server: ', modifiedSentence.decode())
		elapsed = end - start
		print('Elapsed time: {0:.6f}s'.format(elapsed))
		#used the first success as the initial estimatedRTT
		if(numSuccess == 1):
			estimatedRTT = elapsed
		else:
			estimatedRTT = (1 - 0.125) * estimatedRTT + 0.125 * elapsed
		print('EstimatedRTT: {0:.6f}s\n'.format(estimatedRTT))
		totalTime += elapsed
		#looking for largest RTT
		if maxElapsed < elapsed:
			maxElapsed = elapsed
		#looking for smallest RTT
		if i == 1 or minElapsed > elapsed:
			minElapsed = elapsed
	#if timeout occurs the except will catch it
	except Exception:
		print('REQUEST TIMED OUT\n')

print('Max RTT time: {0:.6f}s'.format(maxElapsed))
print('Min RTT time: {0:.6f}s'.format(minElapsed))
print('Average RTT time: {0:.6f}s'.format(totalTime / numSuccess))
print('Packet loss: {0:.2f}%'.format(((numPings - numSuccess)/numPings)*100)) 
clientSocket.close()

