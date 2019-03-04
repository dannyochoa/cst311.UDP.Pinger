#UDPPingerServer.py
#We will need the following module to generate randomized lost packets
import random
from socket import *

#Create a UDP socket
#Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Assign IP address and port number to socket
serverSocket.bind(('', 12000))
serverSocket.settimeout(3)
#number of packet losss
clientLoss = 0

#packet number
i = 0
while True:
	try:
		#Generate random number in the range of 0 to 10
		rand = random.randint(0,10)
		#Receive the client packet along with the address it is coming from 
		message, address = serverSocket.recvfrom(1024)
	
		#index 0 = segment
		#index 1 = time
		#index 2 = msg
		msg = message.decode().split(',')
		#to find the time difference it cannot be the first packet
		if i != 0 :
			#previous time and current time makes elapsed time
			elapsedTime =float(msg[1]) - float(prevTime)
			# if the elapsed time is >= 1 sec a packet lost occur last packet
			if elapsedTime >= 1 :
				print("Packet {} lost".format(i-1))
				clientLoss += 1
		prevTime = float(msg[1])
		i += 1
		#Capitalize the message from the client
		msg[2] = msg[2].encode().upper()
		#If rend is less than 4, we consider the packet lost and do not respond
		if rand < 4:
			continue
		# otherwise, the server responds
		serverSocket.sendto(msg[2],address)
	except Exception:
		#if i == 0 client has not sent anything
		if i!= 0:
			print("Client has stopped sending messages")
			print('Packet loss: {0:.2f}% \n'.format(clientLoss  *10))
			clientLoss = 0
			i = 0


