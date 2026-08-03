import random
b=[1,2,3,4,5,6,7,8,9]
po=['X','O']
def display ():
      print('                 ',b[0], "|", b[1], "|", b[2])
      print("                 ---------")
      print('                 ',b[3], "|", b[4], "|", b[5])
      print("                  ---------")
      print('                  ',b[6], "|", b[7], "|", b[8])
display()
print(' choose the position accordingly')
rdm=random.choice(po)
print(' your turn to',rdm)
def winner():
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for i in win:
        if b[i[0]] == b[i[1]] == b[i[2]]:
            return True

    return False
while True:
    pos=int(input('enter position '))
    if pos not in b:
        print(' enter position correctly')
    elif b[pos-1] in po :
        print(' place is all ready occupied')
    else:
        b[pos-1]=rdm
        if winner():
            display()
            print("🎉 Congratulations! You won!")
            break
        while True :
              rdm1=random.randint(1,9)
              if b[rdm1-1] not in po:
                    break
        
        if rdm=='X':
         b[rdm1-1]='O'
         display()
         if winner():
               print("💻 Computer won!")
               break
        else:
            b[rdm1-1]='X'
            display()
            if winner():
                print("💻 Computer won!")
                break
    if all(i in po for i in b):
             print("Match Draw!")
             break