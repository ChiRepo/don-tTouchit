x=300
print('Globally declared default:',x)
l=[]
l_2=[]
def myfunc():
    global x
    x=200
    print('Inside define Edited:',x)
    while True:
        x=100
        print('in while loop:',)
        while x:
            l.append(x)

            if len(l)==10:
                print(l)
                break
        if len(l)==10:
            print(l)
            break
myfunc()
print('End:',x)