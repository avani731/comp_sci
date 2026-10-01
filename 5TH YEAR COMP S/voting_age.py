print('do you live in athlone?')
A =  input('Y or N:')
if A=='N':
    print('you must live in athlone to vote')
else:
    print('ok')
B=input('how old are you:')
Bint = int(B)
if (Bint==18)or(Bint>18):
  print('you are eligible to vote')
else:
    print('you must be 18 or older to vote')
