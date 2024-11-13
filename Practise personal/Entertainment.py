import random
from colorama import Fore
str1='Upgrading\n'
str2='passing upgrade\n'
while True:
    r=random.randint(1,2)
    if r==1:
        print(Fore.GREEN,f'Status:{str1}',Fore.RESET)
        upgrade_level_b = 1
        upgrade_cost_b = 10000
        print('Upgrade cost for level',Fore.RED,upgrade_level_b,Fore.RESET,'is',Fore.RED,upgrade_cost_b,'$',Fore.RESET,'.')
        upgrade_level = 1
        upgrade_cost = 10000
        def default(u):
            upgrade_level=1
            upgrade_cost=10000
            Total=[]
            for i in range(0,u-1):
                upgrade_cost += 5000
                upgrade_level += 1
                Total.append(upgrade_cost)
                print('Upgrade for level', Fore.MAGENTA, {upgrade_level}, Fore.RESET, 'which costs:', Fore.MAGENTA,{upgrade_cost}, '$', Fore.RESET, Fore.GREEN, '("D O N E").', Fore.RESET)
            for i in Total:
                print(Total)
        u=int(input('\nWhat level you want to upgrade?\n\nNote: Default level will be always 1.\n::Enter number here ---->::'))
        for i in range(0,(u-1)):
            upgrade_cost+=5000
            upgrade_level+=1
            print('Upgrade cost for level',Fore.BLUE,{upgrade_level},Fore.RESET,'is',Fore.BLUE,{upgrade_cost},'$',Fore.RESET,'.')
        print(f'Do you want to proceed?\n',Fore.RED,'Note: Only answer in Y (yes) / N (no).\n',Fore.RESET)
        user = input('::Enter your answer here -----(Y/N)--->::')
        if user==('y'or 'Y'):
            default(u)
        else:
            print(Fore.RED,f'\n{str2}',Fore.RESET)
            pass
    elif r==2:
        print(Fore.RED,f'\nStatus:{str2}',Fore.RESET)
        pass