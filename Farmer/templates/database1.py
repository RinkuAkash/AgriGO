import MySQLdb

class DataBaseOperations():

	def __init__():
		pass

	def insert_into_table_users(data_dict):
		new_connection = MySQLdb.connect('localhost','root','akash198','farmerapp')
		new_cursor = new_connection.cursor()
		# write your SQL statement below.
		statement = "insert into ,users(username, password) values('"+data_dict['username']+"','"+data_dict['password']+"');"
		new_cursor.execute(statement)
		new_connection.commit()
		new_connection.close()
		return True
