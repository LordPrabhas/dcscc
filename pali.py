def is_palindrome(number):
    # Convert the number to a string
    str_num = str(number)
    # Check if the string is the same when reversed
    return str_num == str_num[::-1]

# Input from the user
num = int(input("Enter a number: "))

# Check and display if it's a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
