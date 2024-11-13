import mysql.connector as mysql


# Function to connect to the database
db=mysql.connect(host='localhost',
        user='root',
        password='Chin_191074',
        database='hospitaldb',
        auth_plugin='mysql_native_password'
        )

def create_users_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255))")

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

def add_doctor(cursor, docid, name, specialisation, age, address, monthly_salary):
    l=[docid, name, specialisation, age, address, monthly_salary]
    query = "INSERT INTO doctors (docid, name, specialisation, age, address, monthly_salary) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,l)
    cursor._connection.commit()

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

def delete_patient(cursor, pid):
    l=[pid]
    query = "DELETE FROM patients WHERE pid = %s"
    cursor.execute(query,l)

def delete_doctor(cursor, docid):
    l=[docid]
    query = "DELETE FROM doctors WHERE docid = %s"
    cursor.execute(query,l)

def display_menu():
    print("======================= Hospital Management System Menu ===========================")
    print("                        1. Add Patient                                             ")
    print("                        2. Display Patients                                        ")
    print("                        3. Add Doctors                                             ")
    print("                        4. Display Doctors                                         ")
    print("                        5. Delete Patients                                         ")
    print("                        6. Delete Doctors                                          ")
    print("                        7. Exit                                                    ")

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
            register_user(cursor, username, password)
            print("\nRegistered successfully!\n")

        elif choice == '2':
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            logged_in = login_user(cursor, username, password)
            if logged_in:
                print('Connecting to Database. Please be patient...\n')
                if db.is_connected():
                    print('Connected to Hospital Database.\n')
                    break
                else:
                    print(mysql.connection.errors)
            else:
                print("\nLogin failed. New ID detected. Registration recommended!\n")
        else:
            print('Invalid query.\n', {mysql.connection.errors}, '\n')
            break
def main2():
    create_tables(cursor)
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        #For Patients table.
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
            cursor.execute('select * from patients')
            patq = cursor.fetchall()
            for patients in patq:
                print(patients)
            print('\nData Retrived: ',cursor.rowcount)
            pid = int(input("Enter Patient ID to delete: "))
            delete_patient(cursor, pid)
            print("\nPatient deleted successfully!\n")
            db.commit()

        elif choice == '6':
            cursor.execute('select * from doctors')
            doc = cursor.fetchall()
            for di in doc:
                print(di)
            print("\nPatient deleted successfully!\n")
            docid = int(input("Enter Doctor ID to delete: "))
            delete_doctor(cursor, docid)
            print("\nDoctor deleted successfully!\n")
            db.commit()

        elif choice == '':
            print("\nExiting...\n")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    db.commit()
    db.close()

if __name__ == "__main__":
    #login()
    main2()
