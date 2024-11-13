import mysql.connector as sqlcon
conn=sqlcon.connect(host='localhost',user='root',password='Chin-3003206',auth_plugin='mysql_native_password')
cursor=conn.cursor()
def show_databases():
    cursor.execute('show databases')
    print('\nThe available databases are:\n')
    for a in cursor:
        print(a)
show_databases()
u=input('\nEnter your name of database here: ')
con2=sqlcon.connect(host='localhost',user='root',password='Chin-3003206',database=str(u),auth_plugin='mysql_native_password')
cur=con2.cursor()
if con2.is_connected():
    print(f'\nSuccessfully connected to {u}. Ready to go!')
else:
    print(sqlcon.Error)
u=input('Enter the values for "menu" table:\n')
cmd='insert into menu(m_id,m_name) values(%s,%s)'
value=tuple(u)
cur.executemany(cmd,value)
cur.fetchall()
con2.commit()
print(cur.rowcount,'Rows affected.')