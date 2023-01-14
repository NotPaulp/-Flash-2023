#ручной ввод
n,k=map(int,input().split(' '))
scooters=0
current=int(input())
next1=current
for i in range(n-1):
    next2=int(input())
    if next2-current<=k:
        next1=next2
    elif next2-next1<=k:
        current=next1
        next1=next2
        scooters+=1
    else:
        print(-1)
        break
else:
    print(scooters+1)

#из файла
f=open('1007.txt','r')
f=f.read().split(' \n')
n,k=map(int,f[0].split(' '))
f.pop(0)
f.pop(len(f)-1)
for i in range(len(f)):
    f[i]=int(f[i])
f=sorted(f)
scooters=0
current=int(f[0])
next1=current
for i in range(1,n):
    next2=int(f[i])
    if next2-current<=k:
        next1=next2
    elif next2-next1<=k:
        current=next1
        next1=next2
        scooters+=1
    else:
        print(-1)
        break
else:
    print(scooters+1)