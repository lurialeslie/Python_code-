han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    #print("Line:" ,line)
    #if line == "" :
    #    print("Blank line")
    #    continue
    wds = line.split()
    #print("words:" ,wds)
    #Guardian
    # if len(wds) < 1 :
    #    continue
        #Guardian stronger
    # if len(wds) < 3 :
    #    continue
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != "From" :
        continue
    print(wds[2])
