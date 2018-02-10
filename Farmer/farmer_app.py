from flask import Flask, session, render_template, redirect, request, url_for, flash
import socket, os, MySQLdb
from check_login_ import check_login
from database2 import DataBaseOperations


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def main():
	return redirect(url_for("login"))

@app.route('/register', methods = ['GET', 'POST'])

def register():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		databaseobj = DataBaseOperations()
		databaseobj.insert_into_table_users({'username': username,
						'password': password})
		return redirect(url_for('login', name=username))
	return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])

def login():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		status = check_login(username, password)
		if status:
			session['username']=username
			return redirect(url_for('dashboard'))
		else:
			return render_template('login.html')
	return render_template('login.html')

@app.route('/dashboard', methods = ['GET','POST'])

def dashboard():
    data={}
    data['name'] = session['username']
    new_connection = MySQLdb.connect('localhost','root','akash198','farmerapp')
    statement = "select userfrom,msg from messages where userto='"+data['name']+"';"
    new_cursor = new_connection.cursor()
    new_cursor.execute(statement)
    result = new_cursor.fetchall()
    data['messages']=result
    if request.method == 'POST':
        s = socket.socket()
        s.connect(("127.0.0.1",7893))
        print(data['name']+"-"+request.form['type_msg'])
        s.send(str.encode(data['name']+"-"+request.form['type_msg']))
        s.close()
    return render_template('dashboard.html', data=data)

@app.route('/home')
def home():
	return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
