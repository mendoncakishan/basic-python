# # # print the num is its a even num

# while True:
#     try:

#     k=int(input("enter a int:"))
#     if k % 2 == 0:
#         print("even num")
#     else:
#         print("odd num")
#     except ValueError:
# print("kk")

while True:
    try:
        k = int(input("Enter an integer: "))
        if k % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
