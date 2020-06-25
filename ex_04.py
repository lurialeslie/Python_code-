def computepay(h,r):
    if h > 40 :
        gross_pay = ((h - 40) * r * 1.5) + ((h - 5) * r)
        return gross_pay
    else:
        gp = h * r
        return gp

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r= float(rate)
p = computepay(h,r)
print(p)
