text=input("Enter a line of text: ")
wordlist=list()
wordcount=dict()
count=0
highestwords=list()
wordlist=text.split()
for words in wordlist:
    wordcount[words]=wordcount.get(words,0)+1
for words in wordcount:
    if wordcount[words]>count:
        count=wordcount[words]
for words in wordcount:
    if wordcount[words]==count:
        highestwords.append(words)
print(wordcount)
print(highestwords,"appears a toname = input("Enter file:")
handle = open(name)
emaildict=dict()
emaillist=list()

for line in handle:
    if line.startswith("From "):
        words=line.split()
        email=words[1]
        emaildict[email]=emaildict.get(email,0)+1
bigemail=0
bigcount=0
        
for k,v in emaildict.items():
    if v>bigcount:
        bigemail=k
        bigcount=v

print(bigemail,bigcount)tal of",count,"times.")