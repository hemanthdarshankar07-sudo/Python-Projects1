n=int(input('enter.....'))
orginal=n
reverse=0
while n>0:
     s=n%10
     reverse=reverse*10+s
     n=n//10
if reverse==orginal :
    print('true')
else:
    print('false')