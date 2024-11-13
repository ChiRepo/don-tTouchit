l=[]
def menu():
    while True:
        print('choose your option.\n')
        print('1. POP')
        print('2. Push')
        print('3. Exit')
        choice = int(input('Enter your choice: '))
        if choice==1:
            pop()
        elif choice==2:
            push()
        elif choice==3:
            print('Exiting...')
            break
        else:
            print(EOFError)

def push():
    u=int(input('Enter the element you wanna push in stack: '))
    l.append(u)
    print('Element pushed successfully.')
def pop():
    print(f'The list before: {l}')
    u = int(input('Enter the element you want to pop: '))
    for i in range(len(l)):
        pop=l.pop()
        if pop == u:
            print('element popped successfully.')
            break

menu()