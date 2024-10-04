number=int(input('Enter your number-'))
original_number=number
reverse_number=0
while number>0:
    digit=number%10
    reverse_number=reverse_number*10+digit
    number//=10
if original_number==reverse_number:
    print(original_number,'Is a Palindrome')  
else:
    print(original_number,'Is not a Palindrome')    