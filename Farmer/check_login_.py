import MySQLdb
def check_login(username, password):
    new_connection = MySQLdb.connect('localhost','root','akash198','farmerapp')
    new_cursor = new_connection.cursor()
    statement = "select password from regestered where user='"+username+"';"
    try:
        new_cursor.execute(statement)
    except:
        print("Sorry no Users")
    results = new_cursor.fetchall()
    print(results)
    for row in results:
        if row[0] == password:
            new_connection.close()
            print("got user")
            return True
    print("No user")
    return False
