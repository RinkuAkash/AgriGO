import MySQLdb

class DataBaseOperations():

	def __init__():
		pass

	def insert_into_table_users(data_dict):
		new_connection = connection()
		new_cursor = new_connection.cursor()
		# write your SQL statement below.
		statement = "insert into ,users(username, password) values('"+data_dict['username']+"','"+data_dict['password']+"');"
		new_cursor.execute(statement)
		new_connection.commit()
		new_connection.close()
		return True

	def check_login(username, password):
        new_connection = connection()
        statement = "select password from users where username='"+username+"';"
        new_cursor = new_connection.cursor()
        try:
            new_cursor.execute(statement)
        except:
            print("Sorrry no user")
        results = new_cursor.fetchall()
        for row in results:
            if password == row:
                return True
        return False
        
		# we need to add rest code here to get values and validate.
        #This code cannot handle redundant users. Fatal errors for two same usernames.

	def connection():
		conn = MySQLdb.connect('localhost','root','passkey','farmerdb')
		return conn





        
        
         
