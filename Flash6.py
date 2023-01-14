c=['0','1','2','3','4','5','6','7','8','9','a','b','c']
for a in range(1,10000):
    l=False
    for x in range(0,13):
        for y in range(0,13):
            m=int('2'+c[y]+'23'+c[x]+'5',15)
            n=int('67'+c[x]+'9'+c[y],13)
            if (m+a)%n==0:
                print(a)
                l=True
                break
        if l:
            break
    if l:
        break
