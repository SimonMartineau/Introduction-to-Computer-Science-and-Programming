# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_ps1.pdf
# Problem Set 1
# Name: Simon Martineau
# Time Spent: 0:45
# Section a:

remaining_balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))
minumum_monthly_payment_rate = float(input('Enter the minimum monthly payment rate as a decimal: '))
total_paid = 0.00
for month in range(1,13):
    minimum_monthly_payment = round(minumum_monthly_payment_rate * remaining_balance,2)
    principle_paid = round(minimum_monthly_payment - annual_interest_rate / 12.0 * remaining_balance,2)
    remaining_balance = round(remaining_balance - principle_paid,2)
    print('Month: ', month)
    print('Minimum monthly payment: $' , minimum_monthly_payment)
    print('Principle paid: $' , principle_paid)
    print('Remaining balance: $' , remaining_balance)
    total_paid += minimum_monthly_payment
print('RESULT')
print('Total amount paid: $' , total_paid)
print('Remaining balance: $', remaining_balance)


# Problem Set 1
# Name: Simon Martineau
# Time Spent: 1:00
# Section b:

balance = float(input('Enter the outstanding balance on your credit card: '))
annual_credit_card_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_payment = 0.00
total_paid = 0.00
running_balance = float(balance)
months = 0

while (total_paid < running_balance):
    total_paid = 0
    running_balance = balance
    monthly_payment += 10
    for month in range(1,13):
        running_balance = round(running_balance * (1 + annual_credit_card_interest_rate / 12.0) - monthly_payment,2)
        months = month
        if (total_paid > running_balance):
            break

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ',monthly_payment)
print('Number of months needed: ', months)
print('Balance:' , running_balance)

# Problem Set 1
# Name: Simon Martineau
# Time Spent: 1:30
# Section c:

balance = round(float(input('Enter the outstanding balance on your credit card: ')),2)
annual_credit_card_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_payment = .00
running_balance = balance
months = 0
min_monthly_payment = round(balance/12.00,2)
max_monthly_payment =  round((balance * (1 + (annual_credit_card_interest_rate / 12.0)) ** 12.0) / 12.0)

while abs(running_balance) >= 0.12:
    monthly_payment = round(0.5*(min_monthly_payment + max_monthly_payment),2)
    running_balance = balance
    for month in range(1,13):
        running_balance = round(running_balance * (1 + annual_credit_card_interest_rate / 12.0) - monthly_payment,2)
        months = month
        if abs(running_balance) <= 0.12:
            break;
    if(running_balance < 0):
        max_monthly_payment = monthly_payment
    elif(running_balance > 0):
        min_monthly_payment = monthly_payment
    

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ',monthly_payment)
print('Number of months needed: ', months)
print('Balance:' , running_balance)

