A = input('enter the amount of bill:')
A= float(A)
B = 2000*0.15
C = 1500*0.10
D = 1000*0.05
if A>= 2000:
    print('the discount amount is:',B)
elif B>=1500:
    print('the discount amount is:',C)
else:
    print('the discount amount is:',D)