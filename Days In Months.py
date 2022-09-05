def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "True"
      else:
        return "False"
    else:
      return "True"
  else:
    return "False" 







def days_in_month(chosen_year, chosen_month):
  leap = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  chosen_year = year
  chosen_month = month -1
  days = month_days[chosen_month] 
  if leap == "True":
    days = days + 1
  
#   days = chosen_month[month]

  return f"{days}"


  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)






