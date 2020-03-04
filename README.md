# Weekly-Pay-Calculator

Description:

The Weekly Pay Calculator is a simplistic program written in Python language, used for determining an employee's average weekly pay. The use of this programs allows average people to simply enter the numbers they know and come up with a rough figure for their pay without having to inquire with their organization or scour their previous paychecks.


Instructions:

To use the Weekly Pay Calculator, you will require three pieces of key information:

1. The hourly wage for the employee in question.
2. The estimated amount of hours the employee receives in a given week.
3. Any amount of overtime hours the employee would receive in a given week.

Upon running the program, it will render for the user a fairly simple request:

"What is your Hourly Wage?"

Once the user has received this message the program is ready for input, and the user may enter the desired rate of pay for calculation. This variable has been set as a 'floating' variable, allowing for the use of decimal numbers (cents) that are inherent to currency.

After the employee's wage has been entered, a secondary message will appear to the user:

"Regularly, how many Hours do you receive in a week?"

Here, the user will be prompted to enter the average number of hours the employee would receive in a given week. This variable has been set to a numeric 'integer' variable, due to work hours usually being counted by whole numbers (hours), and not decimals (minutes). Once the number of hours has been entered, this variable is ready for use and may then be entered into the programs calculations.

Once the user has input the employee's average hours for the week, the program will prompt the user for one more piece of information:

"Do you have any Overtime Hours?"

This option was added to allow those who pursue their work hours vigorously to also add in any overtime hours (and thusly, overtime pay) that may have accrued during the week.The variable for this option was also made into a 'floating' variable, like pay, to account for partial overtime hours that would be mathematically represented as decimal numbers. It is important to note that the program is expecting a number to be entered as this stage, and will not accept text-based 'string' entries as an answer, e.g. "No." or "I do not receive overtime."

Once all three pieces of information have been entered, the program will use the given variables in it's equation and calculate the amount of pay the employee should be making per week, based on the variables provided. Once the program has calculated the employee's pay, it will render this message:

"Your weekly pay is: $_____"

This summary will provide the user with the exact amount of pay that the employee should receive every week. If the user wishes to use the program again, or experiment with different variables, simply restart the program, and the first message will appear again.


Errors or Bugs:

As of current, there are little to no errors that have been encountered with this program that would prevent it's effective use. However, the one error that has been encountered is when a use attempts to input a 'string' variable for the secondary message. Upon attempting this the program will encounter an error and fail.


Fixes and Updates:

Even though I am fairly satisfied with the program as it is, there's no reason not to improve upon it's design. Below are a list of future improvements I intend to make as the project progresses forward:

1. I intend to prevent the failure of the program on the second question by simply restating the question to require a different answer. "How many hours of overtime do you have?" will logically prompt a numeric response from the user, avoiding the error and failure when text is entered instead.
2. I believe I could make the entire program more attractive and appealing to the user by broadening it's purpose and use. Rather than simply calculating the employee's pay for a week, it may be wiser to allow the user to select and customize the pay period they want to calculate, such as including options for weekly, biweekly, monthly, or annual pay.
3. I also believe I can make the program more accurate and realistic by including an option for the employee's tax deduction per paycheck. This should allow the program to work with far more realistic numbers and allow the user far more confidence in the results.


Coding:

Below I have shown the lines of coding used for the program for further review and critique.

# Define our variables
Wage = float(input("What is your Hourly Wage?"))
Hours = int(input("Regularly, how many Hours do you receive in a week?"))
Overtime = float(input("Do you have any Overtime Hours?"))
Pay = float(Wage * Hours)
Overpay = float(Overtime * (Wage * 1.5))
Total = (round(Overpay + Pay, 2))

# Have program print total as employee's weekly pay
print ("Your weekly pay is: $", Total)
