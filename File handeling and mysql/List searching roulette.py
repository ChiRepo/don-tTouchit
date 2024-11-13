import random as rand
f=open('search_roulette.txt','w')
r=[]
play_time=f.writelines(r)
f.close()
roulette=open('search_roulette.txt','r')
play=roulette.read()
u=int(input('How many numbers you want to play with in Roulette: '))
while True:
    i=rand.randint(0,u)
    r.append(i)
    if len(r)==u:
        break
    else: pass
print('this is roulette',play)