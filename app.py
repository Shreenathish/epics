from flask import Flask, render_template, request
import mysql.connector 
app = Flask(__name__,template_folder=('template'))

def create_table():
    db_path = mysql.connector.connect(host= "127.0.0.1",user = "root",passwd = "nathish31@",database = "python_db")
    if db_path:
        print("connected")
    else:
        print("not connected")
    c = db_path.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mysql (name TEXT, email TEXT,regno VARCHAR(20),year TEXT)''')
    db_path.commit()
    db_path.close()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    regno = request.form['regno']
    year = request.form['YEAR']
    db_path = mysql.connector.connect(host="127.0.0.1",user ="root",passwd = "nathish31@",database = "python_db")

    c = db_path.cursor()
    c.execute("INSERT INTO mysql (name, email,regno,year) VALUES (%s, %s, %s, %s)", (name, email, regno, year))
       
    db_path.commit()
    db_path.close()
    
    return "DATA SUBMITTED SUCESSFULLY"

#nathish naaaaaa
if __name__ == '__main__':
    create_table()
    app.run(debug=True)
