n,m=list(map(int,input().split()))
while m > 0:
    if n % 10==0:
        n=n//10
    else:
        n=n-1
    m-=1

print(n)
