n=int(input())
l1=list(map(int,input().split()))
lst=[0]*n
for i in range(n):
    lst[l1[i]-1]=i+1

print(*lst,sep=' ')  

