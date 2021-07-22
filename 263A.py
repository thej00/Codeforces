lst=[0]*5
for i in range(5):
    lst[i]=list(map(int,input().split()))
for k in range(5):
    for l in range(5):
        if lst[k][l]==1:
            print(abs(k-2)+abs(l-2))
            break