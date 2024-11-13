import random
num=random.randint(0,1000)
for i in range(1,num):
    i=i+1
    if i==num:
        print(f'bye. Number is:{num}')
    print(i)