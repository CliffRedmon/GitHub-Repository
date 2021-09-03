print("Wecome to the tip calculator.")
bill_total = float(input("What was the total bill? $" ))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))
bill_with_tip = tip / 100 * bill_total + bill_total
per_person = bill_with_tip / people
split = str(round(bill_with_tip / people, 2))
split = "{:.2f}".format(per_person)
print("Each person should pay " + "$" + split)

print("Press any key to exit")
