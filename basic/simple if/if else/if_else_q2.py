# wap to check weather the entered value is single value or colection
k=eval(input("enter a value:"))
if isinstance(k, (int, float, complex, bool)):
    print("single value")
else:
    print("multi value")