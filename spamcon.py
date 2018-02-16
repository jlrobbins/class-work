finame = input('Enter the file name: ')
fipseud = open(finame)
spamcount = 0
spamval = 0
for line in fipseud:
    if line.startswith("X-DSPAM-Confidence:"):
        flospam = float(line[20:])
        spamval = spamval + flospam
        spamcount = spamcount + 1
spamcon = spamval / spamcount
print("Average spam confidence: ",spamcon)