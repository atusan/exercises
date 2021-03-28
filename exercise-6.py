# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

input_month = input('Enter the month of the year (Jan - Dec):').lower()
input_day = int(input('Enter the day of the month:'))

if input_month in ('Jan', 'Feb', 'Mar'):
      season = 'Winter'
elif input_month == 'dec' and input_day > 20:
      season = 'Winter'
elif input_month in ('Apr', 'May', 'Jun'):
      season = 'Spring'
elif input_month == 'mar' and input_day > 19:
      season = 'Spring'
elif input_month in ('Jul', 'Aug', 'Sep'):
      season = 'Summer'
elif input_month == 'jun' and input_day > 20:
      season = 'Summer'
else:
    season = 'Fall'
print(f'{input_month} {input_day} is in {season}')





    
    



