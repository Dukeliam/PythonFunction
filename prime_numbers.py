number = int(input("Enter a number:"))

def prime(number):

    for counter in range(2, number):
        if number % counter == 0:
            return (False)
        
        else:
            return (True)
            
print(prime(number))
