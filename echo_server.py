import socket, random, re

PORT = random.randint(6000, 9000)
MSGLEN = 1024
MAX_LISTEN = 5

MEAN_STUFF = ['suck',
				'boo',
				'hate',
				'lame',
				'worst',
				'go away',
				'stink',
				'shut up',
				'mean'
				]

mean_regex = re.compile(r'\b(?:%s)\b' % '|'.join(MEAN_STUFF), re.IGNORECASE)

if __name__ == '__main__':
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('', PORT))
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.listen(MAX_LISTEN)
	
	print 'connecting to port %s' % PORT

	(client, address) = server.accept()

	while True:
		data = client.recv(MSGLEN)
		if data.strip().lower() == 'logout':
			client.send('logged out\n')
			print 'logged out\n'
			client.close()
			break
		# elif any(word in MEAN_STUFF for word in data.split(' ')):
		# 	client.send('fine :(\n')
		# 	print 'logged out\n'
		# 	client.close()
		# 	break
		elif mean_regex.search(data.strip().lower()):
			client.send('fine :(\n')
			print 'logged out'
			client.close()
			break
		elif data.strip().lower() == 'hi':
			client.send('why hello there!\n')
		elif data.strip().lower() == 'there is some updog on the server':
			client.send('what\'s updog?\n') #sorry
		elif data:
			print 'received %s' % data
			client.send(data)
