# Define our variables
Wage = float(input("What is your Hourly Wage?"))
Hours = int(input("Regularly, how many Hours do you receive in a week?"))
Overtime = float(input("Do you have any Overtime Hours?"))
Pay = float(Wage * Hours)
Overpay = float(Overtime * (Wage * 1.5))
Total = (round(Overpay + Pay, 2))

# Have program print total as employee's weekly pay
print ("Your weekly pay is: $", Total)
