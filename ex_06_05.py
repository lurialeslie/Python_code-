text ="X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')
print(numpos)
endpos = text.find('5',numpos)
print(endpos)
num =text[numpos + 1: endpos + 1]
#print(num)
x= float(num)
print(x)
