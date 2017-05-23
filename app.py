from flask import Flask, render_template, json, request
import pymysql
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
	
@app.route('/signUp',methods=['POST', 'GET'])
def signUp():
	conn = pymysql.connect(host='localhost', user='your_username', passwd='your_password', db='your_database_name')
	cursor = conn.cursor()
	try:
	
		# read the posted values from the UI
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		
		# validate the received values
		if _name and _email and _password:
            
            # All Good, let's call MySQL
            
			
			_hashed_password = generate_password_hash(_password)
			print("length hashed password: ", len(_hashed_password))
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
			data = cursor.fetchall()
			
			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'User created successfully !'})
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close() 
		conn.close()
 
if __name__ == "__main__":
	#app.run(host='0.0.0.0')
	app.run(port=5002)
