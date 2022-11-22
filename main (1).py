L = 6
XL = 10
Size = input("Would you like a L pizza or XL pizza?")
if Size == "XL":
  COS = 10
if Size == "L":
  COS = 6
print()
Toppings = input("How many toppings would you like? (1-4)")
if Toppings == "1":
  COT = 1
if Toppings == "2":
  COT = 1.75
if Toppings == "3":
  COT = 2.50
if Toppings == "4":
  COT = 3.35
print()
Subtotal = (COS) + (COT)
TaxNR = (Subtotal)*0.13
Tax = round(TaxNR,ndigits=2)
Total = (Subtotal) + (Tax)
print("Subtotal($):")
print (Subtotal)
print()
print("Tax($):")
print (Tax)
print()
print("Total($):")
print(Total)