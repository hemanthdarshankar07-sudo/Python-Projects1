balance=100000000
pin=861877
n=3
print(' account should contain atleast minmum balance of 2,000:::')
print('======/n atm starting =======')
while True:
   print('========choose accordingly=======')
   print('==1.for..check  balance')
   print('==2.for.deposite')
   print('==3.for.withdraw')
   print('==4.for...Exit')
   print('==5.for.change password or pin')
   user=int(input(' enter  your choice'))
   upin=int(input('enter your pin'))
   if upin==pin:
            print(' correct pasword  ######')
   else:
                n=n-1
                print(n,'# # # number of choice')
                if n==0:
                    print('==*== ATM LOCKED==*==')
                    break
                else:
                    print(' wrong password ')
                    print('enter correct password')
                    continue
   if user==1:
        print(' your current balance is ,..',balance)
   elif user==2:
     depamt=int(input('====enter amount to deposite '))
     if depamt>0:
       balance=balance+depamt
       print(' ===your current balance is **',balance)
     else:
         print('please enter amount to deposite')
   elif user==3:
        wdamt=int(input('====enter amount to withdraw  :::'))
        if balance-wdamt<2000:
              print(' the account balance should be greater than 2,000')
              print(' insufficent balance')
              balance=balance-wdamt
              print('  # your curent balance is =',balance)
              print(balance+wdamt)
              print('-' ,wdamt)
              print('=', balance)
   elif user==4:
       print('THANK YOU==for using OUR ATM=')
       break
   elif user==5:
       pin=int(input(' enter your new password'))
   else:
       print('### plz enter option correctly(ONLY ENTER 0 to 5##) ')
