import time
import mysql.connector as mysql
import platform as pf
import datetime as dt

db=mysql.connect(host='localhost',user='root',password='Chin_191074',database='hospitaldb',auth_plugin='mysql_native_password')

def create_users_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255))")

def create_table_user_login_info(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS uli(User_Name VARCHAR(255), Login_Date DATE, Login_Time TIME)')

def in_table_user_login_info(cursor, User_Name, Login_Date, Login_Time):
    q='insert into uli(User_Name, Login_Date, Login_Time) values(%s, %s, %s)'
    cursor.execute(q,(User_Name, Login_Date, Login_Time))
    db.commit()

def register_user(cursor, username, password):
    l=[username, password]
    query = "INSERT INTO users(username, password) VALUES(%s, %s)"
    cursor.execute(query,l)
    db.commit()

def login_user(cursor, username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    return cursor.fetchone()

def create_tables(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS patients (pid INT PRIMARY KEY, name VARCHAR(255) NOT NULL, age INT, address VARCHAR(255), ph_no varchar(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS doctors (docid INT PRIMARY KEY, name VARCHAR(255), specialisation VARCHAR(255), age INT, address VARCHAR(255), monthly_salary INT)")

def add_patient(cursor, pid, name, age, address, ph_no):
    l=[pid, name, age, address, ph_no]
    query = "INSERT INTO patients (pid, name, age, address, ph_no) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,l)
    db.commit()

def add_doctor(cursor, docid, name, specialisation, age, address, monthly_salary):
    l=[docid, name, specialisation, age, address, monthly_salary]
    query = "INSERT INTO doctors (docid, name, specialisation, age, address, monthly_salary) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,l)
    db.commit()

def display_doctors(cursor):
    print('\nList of doctors:')
    query='select * from doctors'
    cursor.execute(query)
    f=cursor.fetchall()
    for d in f:
        print(d)
        print('\n')
    print(f'Data retrived:{cursor.rowcount}')

def show_patients(cursor):
    cursor.execute("SELECT * FROM patients")
    f=cursor.fetchall()
    for a in f:
        print(a)
        print('\n')
    print(f'Data retrived:{cursor.rowcount}')

def display_menu():
    print("======================= Hospital Management System Menu ===========================")
    print("                        1. Add Patient                                             ")
    print("                        2. Display Patients                                        ")
    print("                        3. Add Doctors                                             ")
    print("                        4. Display Doctors                                         ")
    print("                        5. Exit                                                    ")
    print("                        6. Sign Out                                                ")

cursor = db.cursor()
def login():
    create_users_table(cursor)

    while True:
        print("1. Register")
        print("2. Login")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("\nCreate username: ")
            password = input("Create password: ")
            if username == '' or password == '':
                print('\n',ValueError," Value can't be empty.\n")
                while True:
                    login()
            else:
                pass
            register_user(cursor, username, password)
            print("\nRegistered successfully!\n")

        elif choice == '2':
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            logged_in = login_user(cursor, username, password)
            if logged_in:
                print('\nConnecting to Database. Please be patient...\n')
                if db.is_connected():
                    print('Connected to Hospital Database.\n')
                    create_table_user_login_info(cursor)
                    User_Name = username
                    Login_Date = dt.date.today()
                    Login_Time= dt.datetime.now().strftime('%H:%M:%S')
                    in_table_user_login_info(cursor,User_Name, Login_Date, Login_Time)
                    break
                else:
                    print(mysql.connection.errors)
            else:
                print("\nLogin failed. New ID detected. Registration recommended!\n")
        else:
            print('\nInvalid query. Please check the given choice again.\n')
            while True:
                login()
def main2():
    create_tables(cursor)
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pid=int(input('Enter Patient ID: '))
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            address = input("Enter patient's current living city: ")
            ph_no = input("Enter Patient's phone number: ")
            add_patient(cursor, pid, name, age, address, ph_no)
            print("\nPatient added successfully!\n")
            db.commit()

        elif choice == '2':
            print("\nList of Patients:\n")
            show_patients(cursor)

        elif choice == '3':
            docid=int(input("Enter doctor's ID :"))
            name = input("Enter doctor's name: ")
            specialisation = input("Enter doctor's specialisation: ")
            age = int(input("Enter doctor's age: "))
            address = input("Enter doctor's current living city: ")
            monthly_salary = int(input("Enter doctor's monthly salary: "))
            add_doctor(cursor, docid, name, specialisation, age, address, monthly_salary)
            print("\nDoctor added successfully!\n")

        elif choice == '4':
            display_doctors(cursor)

        elif choice == '5':
            print("\nExiting...\n")
            break

        elif choice == '6':
            print('\nSigning out...\n')
            db.commit()
            login()

        else:
            print("Invalid choice. Please enter a valid option.")

    db.commit()
    db.close()
login()
main2()
print(f'Process completed in {time.process_time()}')
print(f'Date: {dt.date.today()}')
print(f'Completed on device: {pf.platform()}')