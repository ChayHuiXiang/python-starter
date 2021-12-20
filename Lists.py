List=list()
Sum=0
Count=0
Average=0
while True:
    Numberinput=input("Enter a Number: ")
    if Numberinput=="done": break
    else:
        try:
            Number=float(Numberinput)
        except:
            print("INVALID INPUT")
            continue
        List.append(Number)
Sum=sum(List)
Count=len(List)
Average=Sum/Count
print(Sum,Count,Average)