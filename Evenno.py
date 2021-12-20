while True:
    Noinput=input("Enter a Number:")
    try:
        No=float(Noinput)
        break
    except:
        print("INVALID INPUT")
        continue
if No%2==0:
    print(Noinput,"is an even number.")
else:
    print(Noinput,"is an odd number.")