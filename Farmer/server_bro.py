import socket, MySQLdb

s = socket.socket()
port = 7893
s.bind(('127.0.0.1',port))



s.listen(5)
while True:
	client, addr = s.accept()
	message = (client.recv(10240)).decode()
	print(message)
	from_,to_,message_ = message.split('-')
	print('inserting message...')
	statement = "insert into messages(userfrom, userto, msg) values('"+from_+"','"+to_+"','"+message_+"');"
	conn = MySQLdb.connect('localhost','root','akash198','farmerapp')
	cursor_ = conn.cursor()
	cursor_.execute(statement)
	conn.commit()
	conn.close()
