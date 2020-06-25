# Write a program that prompts for a file name
# then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below

fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
fup = inp.upper()
for line in fup:
    if line.endswith("MIND-NUMBING"):
        line = line.strip()
print(fup)


fh = open ("mbox-short.txt")

for ln in fh:
    ly=ln.rstrip()
    print(ly.upper())
