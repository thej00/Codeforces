n,m=list(map(int,input().split()))
lst=list(map(int,input().split()))
ans=0
for i in range(n):
    if lst[i]>m:
        ans+=2
    else:
        ans+=1
print(ans)