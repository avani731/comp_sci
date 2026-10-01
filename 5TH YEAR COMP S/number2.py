A=int(input('enter a number:'))
B=int(input('enter a second number:'))
if (A>B):
    print(f'{A} is the larger number')
elif(A<B):
    print(f'{B} is the larger number')
else:
    print('both number are same')
    
A=int(input('enter a number{1-19}:'))
if (A>19):
    print('too high')
elif (A<19):
    print('thank you')
    
A=int(input('enter a number(10<A)or(A>20):'))
if (A<10)or(A>20):
     print('incorrect ans')
elif(A>10)and(A<20):
    print('thank you!')
    
A=int(input('enter a number(10<A)or(A>20):'))
if(A<10):
    print('too low')
elif(A>10)and(A<20):
    print('correct')
else:
    print('too high')


A=int(input('enter number(1-3):'))
if (A==1):
    print('thank you')
elif(A==2):
    print('well done')
elif(A==3):
    print('correct')
else:
    print('error message')
      