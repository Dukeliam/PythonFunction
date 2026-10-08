num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))


def subtract(num1, num2):
    result = num1 - num2
    
    if (num1 < num2):
        return (num2 - num1)
        
    return result
print (subtract(num1, num2))
