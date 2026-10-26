def calculatetotal(quantity, price):
    total = quantity * price
    return total

totalextprice = 0

while True:
    quantityinput = input("Enter quantity or stop to finish: ")

    if quantityinput.lower() =="stop":
        break 

    quantity = int(quantityinput)
    price = float(input("Enter unit price: $"))

    extprice = calculatetotal(quantity, price)

    print("Quantity:", quantity)
    print("Price: $", formate(price, ".2f"))
    print("Extended price: $", format(extprice, ".2f"))

    totalextprice = totalextprice + extprice

print("Total extended price: $", format(totalextprice. ".2f"))

if totalextprice > 10000:
    discount = totalextprice * 0.10
    finaltotal = totalextprice - discount

    print("Discount: $", format(discount, ".2f"))
    print("Total after discount: $", format(totalextprice, ".2f"))
else:
    print("No discount.")
    print("Total to pay: $", format(totalextprice, ".2f"))
                                        
