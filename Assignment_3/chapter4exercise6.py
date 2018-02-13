def computepay(h,r):
    if h > 40:
        pay = h * r + (h - 40) * r * 0.5
    else:
        pay = h * r
    return pay

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("")
    print("Both entries must be numbers")
    quit()

total = computepay(hours,rate)
print("")
print("Pay $",total)
