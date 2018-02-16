str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
print(colon)
val = str[colon+1:]
float(val)
print(val)