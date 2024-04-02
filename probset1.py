#Part 1: House Hunting

#Entry parameters for a baseline setup

total_cost = float(input("Enter total cost for dream home"))
annual_salary = float(input("Enter your annual salary"))
portion_saved_y = annual_salary*float(input("Enter savings as portion of salary (in decimals)"))
portion_saved_m = portion_saved_y/12
portion_down_payment = total_cost*0.2
current_savings = float(0)
m = 0
r = float(0.07)

#Iteration over months

while current_savings < portion_down_payment:
    m = m+1
    interest_return = float(current_savings*r/12)
    current_savings = current_savings + interest_return + portion_saved_m

#Output of key variables and expected saving time

print(m)
print(current_savings)
print(total_cost)
print(portion_down_payment)
print("At the given price of the house, the downpayment required,and you monthly savings, it will take you", m," months to save up for the downpayment")

####################################################################################

#Part 2: House Hunting

#Entry parameters for a baseline setup

annual_salary = float(input("Enter your annual salary"))
total_cost = float(input("Enter total cost for dream home"))
portion_saved = float(input("Enter savings as portion of salary (in decimals)"))
semi_annual_raise = float(input("Enter semi annual raise as portion of salary (in decimals)"))

portion_down_payment = total_cost*0.25
current_savings = float(0)
m = 0
r = float(0.04) 

#Iteration over months with increase in annual salary every 6 months

while current_savings < portion_down_payment:
    m = m+1
    portion_saved_m = (portion_saved*annual_salary)/12
    interest_return = float(current_savings*r/12)
    current_savings = current_savings + interest_return + portion_saved_m
    biyearly_increase = int(m%6)
    if biyearly_increase == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)

#Output of key variables and expected saving time

print(m)
print(current_savings)
print(total_cost)
print(portion_down_payment)
print(biyearly_increase)
print(annual_salary)
print("At the given price of the house, the downpayment required,and you monthly savings, it will take you", m," months to save up for the downpayment")

####################################################################################
