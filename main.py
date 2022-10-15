#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Write your code below this line 👇
bill = input("what was the total bill?: ")
tip = input("what was the percentage tip?: ")
no_people = input("how many people will split the bill?: ")

#Calculation
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
outcome_pay = ((int(bill) / int(no_people)) * (1 + (int(tip)/100)))
#opr = round(outcome_pay,2)
message = f"Each person should pay: ${outcome_pay:.2f}"
print(message)
