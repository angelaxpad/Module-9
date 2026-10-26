def calculate_gross_pay(hours, payRate):
    if hours > 40:
        regularPay = 40 * payRate
        overtimePay = (hours - 40) * payRate * 1.5
        grossPay = regularPay + overtimePay
    else:
        grossPay = hours * payRate

    return grossPay


while True:
    lastName = input("Enter employee's last name or stop to finish: ")

    if lastName.lower() == "stop":
        break

    hours = float(input("Enter hours worked: "))
    payRate = float(input("Enter hourly pay rate: $"))

    grossPay = calculate_gross_pay(hours, payRate)

    print("Employee:", lastName)
    print("Hours worked:", format(hours, ".2f"))
    print("Hourly pay rate: $", format(payRate, ".2f"))
    print("Gross pay: $", format(grossPay, ".2f"))

  
