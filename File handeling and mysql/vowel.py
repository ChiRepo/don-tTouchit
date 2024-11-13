str='aeiouAEIOU'
l=list(str)
print(l)
def search():
    u=input('Enter sentence to check: ')
    for i in range(len(l)):
        v_count=0
        for j in u:
            if l[i]==j:
                v_count+=1
        print(l[i],'_____________',v_count)