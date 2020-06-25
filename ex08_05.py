
#8.5 Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the following line:
#You will parse the From line using split() and print out the second word in the line
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    #print("line:" ,line)
    wds = line.split()
    print(wds[1])
    count = count + 1
    #print(count)

print("There were", count, "lines in the file with From as the first word")
