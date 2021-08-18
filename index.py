label = 'Welcome to Public Bank ATM'
chances = 3
balance = 999.999
password = 1234
username = 'User'
active = True
content = '\nWelcome '+username+'!\nEnter 1 for Balance\nEnter 2 to Cashout\nEnter 3 to Transfer\nEnter 4 to Cancel'

def quest():
  quest = input('Would you like to make another transaction?(Yes/No)\n')
  if quest.lower() not in ['yes', 'y', 'yeah', 'okay']:
    print('Thanks for using Public Bank ATM')
    return 0
  
print(label)
while active: 
  try:
    pin = int(input('Enter your 4-digit PIN\n'))
    if pin != password:
      chances -= 1
      print('PIN incorrect\nTry again, you\'ve got',chances,'chances')
      if chances == 0:
        print('Try again in an hour.')
        active = False
    else:
      print(content)
      try:
        response = int(input(''))
        if response == 1:
          print(f'Your balance is : {balance}')
          if quest() == 0 :
            active = False
          else:
            active = True
        elif response == 2:
          try:
            amountToWithdaw = int(input('Enter Amount to Withdraw\n'))
            print(f'Transaction in progress...')
            if balance < amountToWithdaw:
              print('Insufficient Funds')
            else:
              balance -= amountToWithdaw
              print(f'Current Balance : {balance}')
              if quest() == 0 :
                active = False
              else:
                active = True
          except ValueError:
            print('Invalid entry')
        elif response == 3:
          account = input('Enter Valid Recipient Bank Account Number\n')
          try:
            amountToTransfer = int(input('Enter Amount to Transfer\n'))
            print(f'Transaction in Process...')
            if balance < amountToTransfer:
              print('Insufficient Funds')
            else:
              balance -= amountToTransfer
              print(f'Transaction Complete.\nCurrent Balance : {balance}')
              if quest() == 0 :
                active = False
              else:
                active = True
          except ValueError:
            print('Invalid entry')
        elif response == 4:
          print('Thanks for checking out Public Bank ATM')
          active = False
      except ValueError:
        print('Invalid entry')
        active = False
  except ValueError:
        print('Invalid Entry')
        chances -= 1
        print('You\'ve got',chances,'chances')
        if chances == 0:
         print('Try again in an hour.\nThanks for checking out Public Bank ATM')
         active = False
