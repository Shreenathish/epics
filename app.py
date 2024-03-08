import mysql.connector as sql
import datetime as dt
date = dt.datetime.now()

class authorization():

    def __init__(self,user_name,password,category,status):
        self.user_name = user_name
        self.password = password
        self.category = category
        self.status = status
        self.database_connection()

    def database_connection(self):
        self.path = sql.connect(host= "127.0.0.1",user = "root",passwd = "nathish31@",database = "form")
        self.cursor = self.path.cursor()
        self.create_table_for_authorization()
        
    def create_table_for_authorization(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS authorization(user_id INT NOT NULL AUTO_INCREMENT,user_name VARCHAR(20),password VARCHAR(20),log_detail DATETIME,category VARCHAR(20),status VARCHAR(20),PRIMARY KEY(user_id))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS log_base(user_id INT NOT NULL AUTO_INCREMENT,user_name VARCHAR(20),log_in DATETIME,PRIMARY KEY(user_id))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS category(user_id INT NOT NULL AUTO_INCREMENT,user_name VARCHAR(20),category VARCHAR(20),PRIMARY KEY(user_id))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS status(user_id INT NOT NULL AUTO_INCREMENT,user_name VARCHAR(20),status VARCHAR(20),PRIMARY KEY(user_id))')
        self.path.commit()

    def insert_into_table(self,detail):
        self.cursor.execute('INSERT INTO authorization(user_name,password,log_detail,category,status) VALUES(%s,%s,%s,%s,%s)',(detail.user_name,detail.password,date,detail.category,detail.status))
        self.cursor.execute('INSERT INTO log_base(user_name,log_in) VALUES(%s,%s)',(detail.user_name,date))
        self.cursor.execute('INSERT INTO category(user_name,category) VALUES(%s,%s)',(detail.user_name,detail.category))
        self.cursor.execute('INSERT INTO status(user_name,status) VALUES(%s,%s)',(detail.user_name,detail.status))
        self.path.commit() 

class buy():

    def __init__(self,payment_username,password): 

        self.payment_username = payment_username
        self.password = password
        self.database_connection()

    def database_connection(self):
        self.path = sql.connect(host= "127.0.0.1",user = "root",passwd = "nathish31@",database = "form")
        self.cursor = self.path.cursor()
        self.buy_subcription()
    

    def buy_subcription(self):
            payment_id = int(input("enter the payment id:"))
            payment_username = input("enter the username:")
            pay_info = input("enter the payment info:")
            next = date
            a = 'SELECT * FROM authorization WHERE user_name = %s and password = %s'
            self.cursor.execute(a,(self.payment_username,self.password))
            correct = self.cursor.fetchone()
            if correct:
                self.cursor.execute('CREATE TABLE IF NOT EXISTS buy_subcription(user_id INT NOT NULL AUTO_INCREMENT,payment_id INT,payment_username varchar(20),payment_info VARCHAR(50),next_paymentdate DATETIME,PRIMARY KEY(user_id))')
                self.cursor.execute('INSERT INTO buy_subcription(payment_id,payment_username,payment_info,next_paymentdate)VALUES(%s,%s,%s,%s)',(payment_id,payment_username,pay_info,next))
            else:
                print("WRONG PASSWORD")
                self.buy_subcription()
            self.cursor.execute('UPDATE authorization SET status = %s WHERE user_name = %s and password = %s',(pay_info,payment_username,self.password))
            self.path.commit()


class user_data():
    
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        self.database_connection()
    
    def database_connection(self):
        self.path = sql.connect(host= "127.0.0.1",user = "root",passwd = "nathish31@",database = "form")
        self.cursor = self.path.cursor()
        self.checking()
    
    def checking(self):
        a = 'SELECT * FROM authorization WHERE user_name = %s and password = %s'
        self.cursor.execute(a,(self.user_name,self.password))
        correct = self.cursor.fetchone()
        if correct:
            print("PASSWORD ACCEPTED")
        else:
            print("WRONG PASSWORD")

class update_pass():

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        self.database_connection()
    
    def database_connection(self):
        self.path = sql.connect(host= "127.0.0.1",user = "root",passwd = "nathish31@",database = "form")
        self.cursor = self.path.cursor()
        self.reset()

    def reset(self):
        new = input("enter your new password:")
        a = 'SELECT * FROM authorization WHERE user_name = %s and password = %s'
        self.cursor.execute(a,(self.user_name,self.password))
        self.cursor.fetchone()
        self.cursor.execute('UPDATE authorization SET password = %s where user_name = %s and password = %s ',(new,self.user_name,self.password))
        self.path.commit()
    



if __name__ == '__main__':

    game = True

    while game:

        print("1.for sign up")
        print("2.pass checking")
        print("3.buy subcription")
        print("4.update_pass")
        choice = int(input("enter the choice:"))
        if choice == 1:
            user_name = input("enter the user name:")
            password = input("enter the password:")
            category = input("enter the category:")
            status = input("enter the status:")
            detail = authorization(user_name,password,category,status)
            detail.insert_into_table(detail)

        elif choice == 2:
        
            user_name = input("enter the user name:")
            password = input("enter the password:")
            user_data(user_name,password)

        elif choice  == 3:
            payment_username = input("enter the user name:")
            password = input("enter the password:")
            
            buy(payment_username,password)

        elif choice == 4:
            user_name = input("enter the user name:")
            password = input("enter the password:")

            update_pass(user_name,password)
            




            
    
