from tkinter.messagebox import RETRY
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_PASSWORD'] = os.environ.getenv('DB_PASSWD')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME')
 
mysql = MySQL(app)




@app.route('/')
def index():
    return "My Addition App", 200

@app.route('/env')
def env():
    return f"My ENV is {os.environ.get('Name')}"
@app.route('/health')
def health():
    return '', 200

@app.route('/ready')
def ready():
    return '', 200

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
if __name__ == '__main__':  
   app.run(debug = True, host='0.0.0.0', port= os.environ.get('PORT'))  