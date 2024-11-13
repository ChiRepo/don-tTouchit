import mysql.connector as sqlcon
conn=sqlcon.connect(user='root',host='localhost',database='practicals',auth_plugin='mysql_native_password',password='Chin_191074')
cur=conn.cursor()
def customer():
    lst=[]
    customer_ID=int(input('Enter the ID for customer: '))
    lst.append(customer_ID)
    customer_phone=int(input('Enter the phone number of customer: '))
    lst.append(customer_phone)
    payment=int(input('\nEnter the payment method\n(1) Credit Card_____________(2) Debit Card_____________(3) Online Transaction\n'))
    if payment==1 or 'Credit Card':
        lst.append('Credit Card')
    elif payment==2 or 'Debit card':
        lst.append('Debit Card')
    elif payment==3 or 'Online Transaction':
        lst.append('Online Transaction')
    else:print('Error. Check your indication of the following options, also the spelling(uppercase and lowercase)')
    print(lst)
customer()