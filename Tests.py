rateinput=input("Enter Rate: ")
try:
    rate=float(rateinput)
except:
    print("INVALID INPUT")
    quit()

hoursinput=input("Enter No. of Hours:")
try:
    hours=float(hoursinput)
except:
    print("INVALID INPUT")
    quit()

def computepay(r,h):
    if h>40:
        return 40*r+(h-40)*r*1.5
    else:
        return h*r

pay = computepay(rate,hours)
print("Pay =",pay)