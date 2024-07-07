# wap to check whether the entered int num is single digit or double or 3 digit or more then 3 digit num
while True:
    x = input("Enter a num:")

    if x.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        x = int(x)
        if 0 <= x <= 9:
            print("Entered value is one digit.")
        elif 10 <= x <= 99:
            print("Entered value is two digits.")
        elif 100 <= x <= 999:
            print("Entered value is three digits.") 
        else:
            print("Entered value is more than three digits.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")