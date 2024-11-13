'''l=[67848,7643,34523,4323,23423,1235,98065,64575,10986]
print(l)
search_num=[]
def search_number():
    for i in l:
        if i==search_num:
            print('Element found')


search_num=int(input("Enter the desired number: "))
search_number()'''
import random
while True:
    r = random.randint(1, 2)
    print(r)