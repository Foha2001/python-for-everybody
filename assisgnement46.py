rate=input('Enter rate:')
r=float(rate)
hrs = input("Enter Hours:")
h=float(hrs)

def computepay(h,r):
    if h<=40:
        g=h*r
    else:
        g=(h-40)*1.5*r+40*r
    return g

p = computepay(h,r)

print("Pay",p)
