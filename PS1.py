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
# Time Spent:
# Section b:



# Problem Set 1
# Name: Simon Martineau
# Time Spent:
# Section c:

