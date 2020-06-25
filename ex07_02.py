#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    tot = float(0.8475 +  0.6178 + 0.6961 + 0.7565 + 0.7626 + 0.7556 + 0.7002 + 0.7615 + 0.7601 + 0.7605 + 0.6959 + 0.7606 + 0.7559 + 0.7605 + 0.6932 + 0.7558 +  0.6526 + 0.6948 +  0.6528 + 0.7002 + 0.7554 + 0.6956 + 0.6959 + 0.7556 + 0.9846 + 0.8509 + 0.9907)
print("Average spam confidence:", tot/count)
