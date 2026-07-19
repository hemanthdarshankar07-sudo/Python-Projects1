n=int(input('enter.........:'))
sm=0
orginal=n
while n>0:
      s=n%10
      sm=sm+s**3
      n=n//10
if sm==orginal:
     print('its an armstrong')
else:
       print ('its not armstrong')
 