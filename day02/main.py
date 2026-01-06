print("Welcome to the tip calculator!")

total_bill = float(input("What is the total bill amount?: "))
tip_percentage = float(input("How much tip would you like to give? Percent: "))
amount_of_people = int(input("How many people to split the bill?: "))

tip_percentage /= 100

tip_per_person = (total_bill * tip_percentage) / amount_of_people

print(f"Each person owes ${tip_per_person:.2f}")