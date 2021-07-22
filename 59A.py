s=input()
up=0
low=0
for l in s:
    if ord(l)>96 and ord(l)<123:
        low+=1
    elif ord(l)> 64 and ord(l) < 91:
        up+=1
if up>low:
    print(s.upper())
else:
    print(s.lower())