n=int(input())    
w=[input() for _ in range(n)]
for word in w:
    if len(word)>10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)