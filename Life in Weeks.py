# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#We know that 1 year contains 365 days, 52 weeks and 12  months so we subtract all those factors contained in their yearly age by the factors contained by year 90.

ninety_day_count = 365 * 90
ninety_week_count = 52 * 90
ninety_month_count = 12 * 90

age_days = int(age) * 365
age_weeks = int(age) * 52
age_months = int(age) * 12


total_factors_for_ninety = print(f"You have {ninety_day_count - age_days} days, {ninety_week_count - age_weeks} weeks and {ninety_month_count - age_months} months left")













