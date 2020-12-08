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


count = 0
for year in range(1901, 2001):
  if year==1901:
    day = 2 #  2 stands for Monday
  if is_leap_year(year):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  for i in range(12):
    if (day + months[i])%7 == 0
      count += 1
    else:
      rem = months[i]%7
      day += rem
      if day ==1:
        count += 1

print(count)
