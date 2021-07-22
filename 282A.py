n=int(input())
x=0
for _ in range(n):
    com=input().split('X')
    #print(com)
    if '++' in com:
        x+=1
    elif '--' in com:
        x-=1

print(x)
