# wap to check whether the entered char is upper case lower case or number
x=input("enter a char:")
if 'A'<=x<='Z':
    print("enterd char is upperer case alphabet:")
elif 'a'<=x<='z':
    print("entered char is small letter:")
elif '0'<=x<='9':
    print("enteterd char is number ")
else:
    print("its a special char:")