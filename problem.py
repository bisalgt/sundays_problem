def is_leap_year(year):
  if year%4==0:
    if year%100==0:
      if year%400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


# working code to determine the number of sundays in the 20th century
count = 0
for year in range(1901, 2001):
  if year==1901:
    day = 3
  if is_leap_year(year):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  for i in range(12):
    rem = (day + months[i])%7
    if rem == 1:
      count += 1
      day = 1
    else:
      day = rem
  # print ( i + 1, months[i], day, count)

print(count)

  
