# wap to find  gratest of 3 num
k=int(input("enter first num:"))
m=int(input("enter second num:"))
l=int(input("enter third num:"))
if k>m or k>l:
    print ("first num is greter then second and third")
elif m>k or m>l :
     print ("second num is greter then first and third")
elif l>k or l>m:
      print ("third num is grater then all")