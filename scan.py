import socket
import subprocess
import sys


subprocess.call('clear', shell=True)

server = raw_input("Enter a remote host to scan: ")

serverIP = socket.gethostbyname(server)

print "Scanning..."

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((serverIP, port))
		if result == 0:
			print "Port{}: \t Open".format(port)
		sock.close()
except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

