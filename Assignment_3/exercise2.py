hours = input('enter hours:')
rate = input('enter rate:')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print('error, please enter numeric input')

if fh > 40 :
    regular_pay = fr * fh
    overtime_pay = (fh-40.0) * (fr * 0.5)
    xp = regular_pay + overtime_pay
else:
    xp = fh * fr
print("Pay", xp)
