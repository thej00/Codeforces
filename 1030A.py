n=int(input()) #taking input n
lst=list(map(int,input().split())) #mapping inputs into the list
if lst.count(1) !=0 :
    print('hard')
else:
    print('easy')
