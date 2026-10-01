S=input('enter your total sales for the month:')
S= float(S)
I = S*0.15
T = S*0.05
if S>40000:
    print(f'{S} your intrest is:',I)
elif S<40000:
    print(f'{S} your intrest is:',T)

