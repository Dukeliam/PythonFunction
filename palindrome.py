num = input("Enter 5 digit integer:")

def palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False
        
print(palindrome(num))
