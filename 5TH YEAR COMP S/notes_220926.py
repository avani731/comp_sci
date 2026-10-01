a = 'hel'
b = 'lo'
print(a+b)#string concatenation
result = a+b
print(result*3) #string replication

#variable assignment
#a variable can only link to one value at a time
A = '123'
A = int(A)
B = '123'
C = int(123)
print(C)
# B and C should be different variables

#multiple variable assignment
a=b=c = 10
print(a,b,c)
#you can assign the multiple values to multiple variable at same time
x,y,z =10,20,30
print(x,y,z)

x=10
y = 5
print(x,y) #thonny only remembers the last line of code u have written when the value is changed of the variable like on line 27 

x,y =y,x # it swaps the value of the variable
print(x,y)

x=10
y = 5
print(x,y)
temp = x
x = y #
y = temp # y is assigned the variable temp so y=10
print(x,y)

print('my','name','is','avani')# the commas(,) act like spaces between commands

#print(statement)-seperator
print('my','name','is','avani',sep ='...')#each word is seperated by ellypses
 