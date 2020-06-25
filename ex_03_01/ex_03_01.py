hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
r= float(rate)
if h > 40 :
    np = (h - 5) * r
    sh = (h - 40) * r * 1.5
    gross_pay = sh + np
    print(gross_pay)
else :
    gp = h * r
    print(gp)
