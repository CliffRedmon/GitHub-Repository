#Time until 90
age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {week_remaining} weeks, or {months_remaining} months left."
print(message)

print("Press any key to exit.")
