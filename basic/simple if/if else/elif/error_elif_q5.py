# wap to convert the first char of a string into lower case if its a upper case
# to convert the first char of a string into upper case if its a lower case/
# if it is a char is digit find the power of it
# if its a special char  add five to ascii value and print the chat
k=input("enter a string:")
if 'A'<=k[0]<='Z':
    print("upper case :",ord(chr[0]+32))
elif 'a'<=k[0]<='z':
    print("lower case ",chr(ord[0]-32))
elif '0'<=k<='9':
    print("number kanoo ",int(k[0]**2))
else :
    print(ord(k[0]))