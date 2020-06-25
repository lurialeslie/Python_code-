largest = None
smallest = None
while True:
    num = input("Enter a number:")
    if num == "done" :
        break
    try:
        var = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or var > largest :
        largest = var
    elif smallest is None or var < smallest :
        smallest = var
print("Maximum is", largest)
print("Mininum is", smallest)
