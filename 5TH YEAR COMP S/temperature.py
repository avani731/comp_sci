S = input('enter the temperature of the water:')
S = float(S)
if S > 100:
    print('it is in a gaseous state')
elif S < 0:
    print('it is in solid state')
else:
    print('it is in liquid state')