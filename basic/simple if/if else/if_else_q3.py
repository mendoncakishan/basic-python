# wap to print the reverse string if the length is between 5 to 10 if not print as it is
k=input("enter a string:")
if 5<=len(k)<=10:
    print("revers string is",k[::-1])
else:
    print("string is ",k)