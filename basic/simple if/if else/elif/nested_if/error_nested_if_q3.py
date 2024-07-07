# consoider a student marks in six sun
# find result based of aveg
# find aveg only if student scored more then 35
name=(input("input name:"))
py=int(input("enter marks of py"))
mt=int(input("enter marks of mt"))
sql=int(input("enter marks of sql"))
sel=int(input("enter marks of sel"))
web=int(input("enter marks of web"))
apti=int(input("enter marks of apti "))
if py>=35 and mt>=35 and sql>=35 and sel>=35 and web>=35 and apti>=35:
    avg= (py+mt+sql+sel+web+apti)/6
    print("yout average is :",avg)
    if avg>=80:
        print("macha yako istu vodtiya")
    elif 60<=avg<=79:
        print("secnd class macha:")
    elif 49<=avg<=59:
        print("frinds sari ella:")
    elif 35<=avg<=47:
        print("alak bulak")
    else :
        print("baro yenne hodiva")