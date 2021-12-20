Count=0.0
Total=0.0
Average=0.0
while True:
    Numberinput=input("Enter a number:")
    if Numberinput=="done":
        break
    else:
        try:
            Number=float(Numberinput)
        except:
            print("Invalid Input")
            continue
        Count=Count+1
        Total=Total+Number
Average=Total/Count
print(Total,Count,Average)