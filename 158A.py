n,k=list(map(int,input().split()))
scores=list(map(int,input().split()))
target=scores[k-1]
count=0
for s in scores:
    if s>0 and s>=target:
        count+=1

print(count)