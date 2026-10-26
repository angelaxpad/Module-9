def calculate_mpg(miles, gallons):
    mpg = miles / gallons
    return mpg


totalMiles = 0
totalGallons = 0

while True:
    tripName = input("Enter trip name or stop to finish: ")

    if tripName.lower() == "stop":
        break

    miles = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons used: "))

    if gallons > 0:
        mpg = calculate_mpg(miles, gallons)

        print("Trip:", tripName)
        print("Miles driven:", format(miles, ".2f"))
        print("Gallons used:", format(gallons, ".2f"))
        print("Miles per gallon:", format(mpg, ".2f"))

        totalMiles = totalMiles + miles
        totalGallons = totalGallons + gallons
    else:
        print("Gallons must be greater than zero.")

if totalGallons > 0:
    totalMPG = calculate_mpg(totalMiles, totalGallons)

    print("Total miles:", format(totalMiles, ".2f"))
    print("Total gallons:", format(totalGallons, ".2f"))
    print("Overall miles per gallon:", format(totalMPG, ".2f"))
else:
    print("No valid trips entered.")




Wave
