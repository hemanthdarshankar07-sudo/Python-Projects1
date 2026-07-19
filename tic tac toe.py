import random
list1=['r','p','s']
score=0
for i in range (3):
     h=random.choice(list1)
     print('r for rock ,,s for Scissor  ,,p for paper')
     q=input('enter your choice  ,,')
     if (q=='r' and h=='s' or q=='s' and h=='p' or q=='p' and h=='r') :
        print('you won')
        score=score+1
     else:
         print('you lose')
if score>=2:
                    print ('your the winn')
else:
                      print('your the loser')