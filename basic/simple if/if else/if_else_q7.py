# wap to check weather two variables are pointing toword same memory location or not
k=input("enter a variable:")
m=input("enter second variable:")
if id(k)==id(m) or id(m)==id(k):
    print("entered value memory location is same:")
else:
    print("entered var memory space is diff")
