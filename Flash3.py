import itertools
a=itertools.product('ПОЛИНА', repeat=7)
k=0
for i in a:
    a=0
    p=0
    if i[0]!='А':
        for j in i:
            if j=='А':
                a+=1
            elif j=='П':
                p+=1

    if a==1 and p==1:
        k+=1

