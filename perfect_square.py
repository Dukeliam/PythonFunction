def is_perfect_square(number):
      square_root = number**0.5
      (square_root**2) == number
      if square_root.is_integer():
            return True
      else:
            return False
      
def perfect_square(numbers):
      square = []
      
      for index in numbers:
            if is_perfect_square(index):
                  square.append(index)
      return square
      
print(is_perfect_square(25))

print(perfect_square([23,9,34,16,93,25]))
