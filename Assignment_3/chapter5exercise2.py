Largest = None
Smallest = None
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if Smallest is None or fval < Smallest:
        Smallest = fval
    if Largest is None or fval > Largest:
        Largest = fval

print('max is', Largest)
print('min is', Smallest)
