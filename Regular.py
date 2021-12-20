import re
sum=0
number=0
fh=open("regex_sum_1058212.txt")
for line in fh:
    if re.search("[0-9]+",line):
        for no in re.findall("[0-9]+",line):
            number=int(no)
            sum=sum+number
print(sum)