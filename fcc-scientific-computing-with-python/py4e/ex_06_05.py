str = 'X-DSPAM-Confidence: 0.8475'
colon_pos = str.find(":")
num_str = str[colon_pos + 2:]
num = float(num_str)
print(num)