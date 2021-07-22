n=int(input())
ans=0
k=0
for _ in range(n):
    a,b=list(map(int,input().split()))
    k=k-a+b
    ans=max(ans, k)

print(ans)