hrs = input("Enter Hours:")
h = float(hrs)
rate=input("rate per hour:")
r=float(rate)
if h<=40:
    pay=h*r
if h>=40:
    pays=40*r
    pay=1.5*(h-40)*r +pays
print(pay)
