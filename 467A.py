n=int(input())
ans=0
for _ in range(n):
    i1,i2=list(map(int,input().split()))
    if i2-i1 >= 2:
        ans+=1

print(ans)