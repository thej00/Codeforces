p,m,n=list(map(int,input().split()))
total=0
for i in range(1,n+1):
    total+=(i*p)

if total-m > 0:
    print(total-m)
else:
    print(0)