# wap to check whether candidates are eligable for voting
age=int(input("enter ur age :"))
idproof=input("if you have id type yes or else type no:")
if age>=18:
    print("age accepted:")
    if idproof=='yes' or idproof=='YES':
        print("eligible for voting")
    else:
        print("make a voter id first")
else:
    print("ur under age")
