n=int(input())
count=0
for _ in range(n):
    sol=list(map(int,input().split()))
    if sum(sol)>=2:
        count+=1

print(count)