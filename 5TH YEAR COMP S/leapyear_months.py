A=int(input('enter the month and year:'))
if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
  print('its a Leap year!')
else:
 print('not a leap year:(')