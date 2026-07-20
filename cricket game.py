import random
list1=[0,1,2,3,4,5,6,]
list2=['head','tails']
cs=0
score=0
h1=input('enter head or tails..;')
q=random.choice(list2)
print(q)
n=int(input('no.of overs'))
for i in range(n*6):
  if h1 not in list2 :
     print(' enter only head or tails ')
     continue
  if h1==q:
       print('you are on the strike you got a chance to bat..')
       h=int(random.choice(list1))
       g=int(input('ggggg'))
       if h==g:
           print(' ought    ')
           print( ' computers turn to bat')
           q1=input(' enter ....')
           h1=random.choice(list1)
           if h1==q1:
               print ('wicket  ')
               break
           else:
               cs=cs+h1
       else: 
            score=score+g
  else:
        print('computer is on strike your turn to ball')    
        h=input('enter   ...')
        g= random.choice(list1)
        if h==g:
            print(' wicket')
            hq=input('enter   ...')
            gq= random.choice(list1)
            if hq==gq:
                 print('out  ')
                 break
            else:
                score=score+hq
        else:
            cs=cs+g
if cs<score:
            print(' you are the winner')
            print(' graet')
else :
    print(' you lose ')
    print('  try again')