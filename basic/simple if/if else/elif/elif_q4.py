# wap consider a string print the char present at even index if the char is upper case 
# /print the revers char preesent at odd index of a string if the first char is digit
# / print the reverse string if the first char is a special char 
# /if not print the len of asic value of first char
x=input("enter a char:")
if 'A'<=x[0]<='Z':
    print("upper case and even index is :",x[::+2])
elif 'a'<=x[0]<='z':
    print("lower case and the ",x[1::+2])
elif '0'<=x<='9':
    print("number kanoo reverse hodii",x[::-1])
else :
    print(ord(x[0]))
