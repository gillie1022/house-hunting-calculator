annual_salary = int(input("Enter your annual salary: "))
current_savings = 0
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
rate_input = input("Enter the expected rate of return: ")
if rate_input == "":
    r = .04
else:
    r = float(rate_input)
total_cost = int(input("Enter the cost of your dream home: "))
p_down_input = input("Enter the percent of your home's cost to save as a down payment: ")
if p_down_input == "":
    p = .25
else:
    p = float(p_down_input)

portion_down_payment = int(total_cost * p)

num_months = 0

while current_savings <= int(portion_down_payment):
    current_savings += (annual_salary * portion_saved)/12 + current_savings*r/12
    num_months += 1
print("Number of months: " + str(num_months))