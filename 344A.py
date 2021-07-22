n=int(input())
m=int(input())
c=1
for i in range(1,n):
    l=int(input())
    if l!=m:
        c+=1
    m=l
print(c)

