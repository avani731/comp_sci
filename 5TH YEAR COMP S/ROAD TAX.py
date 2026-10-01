A = input('enter the cost of your bike:')
A = float(A)
if (A >10000):
    print('the road tax is:',(A*0.15))
elif(A>5000)and(A<=10000):
     print('the road tax is:',(A*0.10))
elif(A<=5000):
     print('the road tax is:',(A*0.05))