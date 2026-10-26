def calculateaverage(hits, atbats):
    average = hits / atbats
    return average

playercount = 0

while True:
    lastname = input("Enter player's last name or stop to finish: ")

    if lastname.lower() =="stop":
        break

    hits = int(input("Enter number of hits: "))  
    atbats = int(input("Enter number of at bats: "))

    if atbats > 0:
        average = calculateaverage(hits, atbats)

        print("Last name:", lastname)
        print("Batting average:", format(average, ".3f"))

        playercount = playercount + 1
   else:
        print("At bats must be greater than zero.")

print("Number of players entered:", playercount)
  
