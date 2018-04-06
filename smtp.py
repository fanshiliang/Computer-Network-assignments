from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
username = "fanshiliang1994@gmail.com"
password = "rppvsmtioydlmdkd"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver ='smtp.gmail.com'
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
print "creating web socket"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'
	
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send EHLO command and print server response
ehloCommand = 'EHLO smtp.gmail.com\r\n'
clientSocket.send(ehloCommand)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received form server.'

# Start with auth login with plain
authMsg = "STARTTLS\r\n"
print authMsg
clientSocket.send(authMsg)
recv2 = clientSocket.recv(1024)
print recv2

# Start ssl connection
clientSocket_ssl = ssl.wrap_socket(clientSocket)

# EHLO again
ehloCommand = 'EHLO smtp.gmail.com\r\n'
clientSocket_ssl.send(ehloCommand)
recv2 = clientSocket_ssl.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received form server.'

# send auth information
auth_username = base64.b64encode(username)
auth_password = base64.b64encode(password)
auth = base64.b64encode("\0"+username+"\0"+password)
print auth_username
print auth_password
print auth
# clientSocket.send(auth_username+"\r\n")
clientSocket_ssl.send("AUTH PLAIN "+auth+"\r\n")
recv2 = clientSocket_ssl.recv(1024)
print recv2
# clientSocket.send(auth_password+"\r\n")
# recv2 = clientSocket.recv(1024)
# print recv2
# Send MAIL FROM command and print server response.
clientSocket_ssl.send("MAIL FROM: <fanshiliang1994@gmail.com>\r\n")
recv2 = clientSocket_ssl.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'
	
# Send RCPT TO command and print server response.
clientSocket_ssl.send("RCPT TO: <fanshiliang1994@gmail.com>\r\n")
recv2 = clientSocket_ssl.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

# Send DATA command and print server response.
clientSocket_ssl.send("DATA\r\n")
recv2 = clientSocket_ssl.recv(1024)
print recv2
if recv2[:3] == '250':
	print '250 reply not received from server.'
elif recv1[:3] == '500':
	print '500 The server could not recognize the command due to syntax error.'
elif recv1[:3] == '501':
	print '501 The syntax error was encountered in command arguments.'
elif recv1[:3] == '502':
	print '502 This command is not implemented.'
	
# Send subject message data
clientSocket_ssl.send("Subject: test message\r\n")
clientSocket_ssl.send("From:""< 949631920@qq.com>\r\n")
clientSocket_ssl.send("To:""< fanshiliang1994@gmail.com>\r\n")
clientSocket_ssl.send(msg)

# Send message data.
# clientSocket_ssl.send("SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test\n.\n\r\n")

# # Message ends with a single period.
clientSocket_ssl.send(endmsg)
recv2 = clientSocket_ssl.recv(1024)
print "after sending endmsg: ", recv2
# if recv2[:3] != '250':
# 	print '250 reply not received from server.'
#
# Send QUIT command and get server response.
clientSocket_ssl.send("QUIT\r\n")
recv2 = clientSocket_ssl.recv(1024)
print "after quit: ", recv2
# if recv2[:3] != '250':
# 	print '250 reply not received from server.'

# print "Mail sent"
