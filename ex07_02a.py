print("Hello world")

fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    ln = line.find(":")
    #print(ln)
    numpos = float(line[ln + 2:])
    #print(numpos)
    count = count + 1
    tot = tot + numpos
    average = float(tot/count)
print("Average spam confidence:", average)
#print(count, tot, tot/count)
