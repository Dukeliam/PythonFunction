num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

def divide(num1, num2):

    if(num2 == 0):
        return num2
        
    result = num1 / num2
    
    return result
    
print (divide(num1, num2))
