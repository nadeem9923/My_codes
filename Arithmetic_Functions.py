import math
p = math.pi/6

def show_choices():
 print('\nMenu')
 print('1. Add')
 print('2. Sutract')
 print('3. Multiply')
 print('4. Divide')
 print('5. Sin')
 print('6. Cos')
 print('7. Tan')
 print('8. Log')
 print('9. Pow')
 print('10. Sqrt')


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
def sin(p):
    return math.sin(p)
    
def cos(p):
    return math.cos(p)
    
def tan(p):
    return math.tan(p)

def log(x):
    return math.log(x)
 
def pow(x,y):
    return math.pow(x,y)
    
def sqrt(x):
    return math.sqrt(x)
 

def main():
    while(True):
        show_choices()
        choice = input('Enter choice(1-10): ')
        if choice == '1':
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            print('Sum =', add(x, y))
            
        elif choice == '2':
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            print('Difference =', subtract(x, y))
            
        elif choice == '3':
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            print('Product =', multiply(x, y))
            
        elif choice == '4':
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            if y == 0:
                print('Error!! divide by zero')
            else:
                print('Quotient =', divide(x, y))  
		
        elif choice == '5':
                print ("The value of sine of pi/6 is : ",math.sin(p))
        elif choice == '6':
                print ("The value of cosine of pi/6 is : ",math.cos(p))
        elif choice == '7':
                print ("The value of tangent of pi/6 is : ",math.tan(p))
        elif choice == '8':
                x = int(input('Enter first number: '))
                print ("Natural alogarithm of x is : ",math.log(x))
        elif choice == '9':
                x = int(input('Enter first number: '))
                y = int(input('Enter second number: '))
                print ("Value of x raised to the power of y is: ",math.pow(x,y))
        elif choice == '10':
                x = int(input('Enter first number: '))
                print ("Square root of x is: ",math.sqrt(x))
        else :
                print('Invalid Choice')
                exit();
main()