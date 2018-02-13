str = 'X-DSPAM-Confidence: 0.8475'

col_pos = str.find(":")
print(col_pos)
piece = str[col_pos+1:]
print(piece)
value = float(piece)
print(value)
