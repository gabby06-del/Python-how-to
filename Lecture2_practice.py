#Part A: code to find the number of months it will take to save up for a down payment 
yearly_salary = float(input("What is your starting yearly salary?: "))
portion_saved = float(input("What portion of your salary are you saving?: "))
cost_of_dream_home = float(input("What is that cost of your dream home?: "))
portion_down_payment = 0.25
down_payment= cost_of_dream_home*portion_down_payment
amount_saved = 0.0
r= 0.05
months = 0

while amount_saved < down_payment:
    monthly_return = amount_saved * (r/12)
    amount_saved+= ((yearly_salary/12)*portion_saved)+monthly_return
    months += 1

print(f"Number of months: {months}: current savings = $ {amount_saved:,.2f}")

#Part B: Code to find how many months it will take to save up for a down payment given a semi annual raise 
yearly_salary = float(input("What is your starting yearly salary?: "))
portion_saved = float(input("What portion of your salary are you saving?: "))
cost_of_dream_home = float(input("What is that cost of your dream home?: "))
portion_down_payment= 0.25
down_payment= cost_of_dream_home*portion_down_payment
amount_saved = 0.0
r=0.05
months = 0
semi_annual_raise = 0.03
while amount_saved < down_payment:
    monthly_return = amount_saved * (r/12)
    amount_saved+= ((yearly_salary/12)*portion_saved)+monthly_return
    months += 1
    if months % 6 == 0:
        yearly_salary += yearly_salary*semi_annual_raise
print(f"Number of months: {months}")


#Part C: Given an initial deposit amount, our goal is to find the lowest rate of return that enables us to save enough money for the down payment in 3 years.
initial_deposit= float(input("Initial amount being deposited into account: "))
house_cost=float(800000)
portion_down_payment= float(0.25)
down_payment = house_cost*portion_down_payment
months = 36
num_guess=0
low = 0
high = 1
epsilon= 100
max_savings = initial_deposit * ((1+high/12)**months)

if max_savings < down_payment:
    print("It is not possible to pay the downpayment in three years with this deposit")
    print(f"best interest rate: None")

else:
    while True:
        num_guess += 1
        r = (low+high)/2.0
        amount_saved = initial_deposit * ((1+r/12)**months)
        if abs(amount_saved-down_payment) <= epsilon:
            break
        if amount_saved< down_payment:
            low=r
        else:
            high=r

print(f"best interest rate: {r:.4f}")
print(f"Number of guesses: {num_guess}")

