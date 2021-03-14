# take 2 numbers as input ans print result of X^Y
x = int(input("Enter the number: "))
y = int(input("Enter the number2: "))
z = pow(x,y)
print(z ,end = ' ')

#2>prog to print numbers in list which are divisible by 3:

list = [2,3,4,5,7,9,6]
for number in list:
    if number%3 == 0:
        print(number)
    else:
        print("not ")
    
