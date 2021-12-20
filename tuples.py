fhand=open("romeo.txt")
wordcount=dict()
for line in fhand:
    words=line.split()
    for a in words
        	wordcount[a]=wordcount.get(a,0)+1
            

list=list()
for k,v in wordcount.items():
    list.append((v,k))

newlist=list()
newlist=sorted(list,reverse=True)
print(newlist[:10])