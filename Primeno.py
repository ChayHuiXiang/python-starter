while True:
    Noinput=input("Enter a Number:")
    try:
        No=float(Noinput)
        break
    except:
        print("INVALID INPUT")
        continue
x=1
Remainder=0
Count=0
while True:
    if x==No:
        break
    else:
        Remainder=No%x
        if Remainder==0: Count=Count+1
        x=x+1
if Count==1:
    print(Noinput,"is a prime number.")
else:
    print(Noinput,"is not a prime number.")