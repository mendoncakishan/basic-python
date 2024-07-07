# wap to print 'ee sale cup namde' if nu m is divisible ny 3  ,print'washing powder nirma' if num divisible by 5,"nirma namde is divisible by 3 and 5"
k=int(input("enter a num:"))
if k%3==0 and k%5==0:
    print("nirma namde")
elif k%3==0:
    print("ee sale cup namde")
elif k%5==0:
    print("washing powder nirma")