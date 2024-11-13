f=open('search_number.txt','r')
r=f.readlines()
rng=int(input('Enter the max range: '))
fw=open('search_number.txt','w')
l=[]
n=int(input('Enter the number you want to search: '))
for i in range(0,rng):
    u=int(input('Enter the number in list: '))
    l.append(u)
fw.writelines(str(l))
def search():
    searched_num=0
    for i in range(len(l)):
        if l[i]==n:
            searched_num+=1
    if searched_num==0:
        print('Number is not in the list.')
    else:
        print('Search successful.\nNumber is in the list.')
search()