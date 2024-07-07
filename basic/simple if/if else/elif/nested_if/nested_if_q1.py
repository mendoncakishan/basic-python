# wap to check the entered char is vowel or consonant it can be both upper and lower case
k=input("enter a char:")
if 'A'<=k<='Z' or 'a'<=k<='z':
    if k in 'AEIOUaeiou':
        print("vowel machaaa")
    else: 
        print("its a consonant")
else:
    print("not a char")