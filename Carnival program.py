#Question 5 chatgpt
while True:
    try:
        user_age = int(input("Enter your age: "))
        if user_age < 4 or user_age > 120:
            raise ValueError
        break
    except ValueError:
        print("Invalid age input. Please enter a valid age.")

while True:
    try:
        day_week = int(input("Please enter the day of the week (1 being Monday & 7 being Sunday): "))
        if day_week < 1 or day_week > 7:
            raise ValueError
        break
    except ValueError:
        print("Invalid day input. Please enter a valid day.")

if day_week == 6 or 7:
    ticket_price = 10
elif user_age < 16:
    ticket_price = 7.50
else:
    ticket_price = 10
    if user_age >= 65:
        ticket_price = 5.50

print(f"You have to pay ${ticket_price:.2f}")