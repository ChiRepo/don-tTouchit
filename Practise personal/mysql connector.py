import mysql.connector as sqlcon
con=sqlcon.connect(host='localhost',user='root',password='Chin_191074',auth_plugin='mysql_native_password')
cursor=con.cursor()
print('Which database you want to go in? The list of databases available are:\n')
def show_databases():
    cursor.execute('show databases')
    for a in cursor:
        print(a)
show_databases()
con.commit()
u=input('\nEnter your name of database here: ')
con2=sqlcon.connect(host='localhost',user='root',password='Chin_191074',database=str(u),auth_plugin='mysql_native_password')
cur_2=con2.cursor()
def cmd():
    u=input('\nEnter your SQL command:\n\n')
    cur_2.execute(u)
    rc=cur_2.rowcount
    for a in cur_2:
        print(a)
    print('\nRows affected and executed successfully', rc)
if con2.is_connected():
    print(f'\nSuccessfully connected to {u}. Ready to go!')
else:
    print(sqlcon.Error)
cmd()
u=input('Do you want to write command? y/n: ')
if u=='y':
    cmd()
else:
    print(sqlcon.InterfaceError)