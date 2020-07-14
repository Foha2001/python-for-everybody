largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num is not "done":
        try:
             numin=int(num)
        except:
            print("Invalid input")
    if largest is None:
        largest=numin
    elif largest<numin:
        largest=numin
    if smallest is None:
    	smallest= numin
    elif numin<smallest:
        smallest=numin
    if num == "done" : break
print("Maximum is", largest)
print("Minimum is", smallest)
