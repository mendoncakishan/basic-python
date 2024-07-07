# WAP to print the reversed string

while True:
    x = input("Enter a string: ")

    if x.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        print("Reverse of the string is:",x[::-1])
    except ValueError:
        print("Invalid input. Please enter a valid string or 'exit'.")


# using try catch