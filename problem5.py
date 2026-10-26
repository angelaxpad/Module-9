def calculate_tuition(credit_hours, district_code):
    if district_code == 1:
        tuition = credit_hours * 250
    else:
        tuition = credit_hours * 550

    return tuition


total_tuition = 0

last_name = input("Enter student last name: ")
credit_hours = int(input("Enter credit hours: "))
district_code = int(input("Enter district code (1 = In district, 0 = Out of district): "))

tuition_owed = calculate_tuition(credit_hours, district_code)

print("Student last name:", last_name)
print("Tuition owed: $", tuition_owed)

total_tuition = total_tuition + tuition_owed

print("Total tuition owed: $", total_tuition)

