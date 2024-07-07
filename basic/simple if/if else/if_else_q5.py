# wap to check weather the string is palindrome or not
k=input("enter a string:")
if k==k[::-1]:
    print("string is palindrome:",k)
else:
    print("string is not palindrome:",k)
