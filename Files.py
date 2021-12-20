fhand="I wanna learn python quick and I don't wanna learn python slow/nI wanna learn python quick and I don't wanna learn python slow/nI wanna learn python quick and I don't wanna learn python slow/nI wanna learn python quick and I don't wanna learn python slow"
words=list()
wordlist=list()
for line in fhand:
    words=line.strip()
    for a in words:
        if a not in wordlist:
            wordlist.append(a)
print(wordlist)