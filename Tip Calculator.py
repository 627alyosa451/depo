#Tip Calculator
import time
print('welcome to the tip calculator')
bill =  input('What was the total bill? ')
tip_percentage = input('What percentage tip would you like to give? ')
people = input('How many people to split the bill? ')

#Calculation

tip = float(bill) / 100 * float(tip_percentage)

total = (float(bill) + float(tip))

each_person = float(total) / int(people)

result = round(each_person, 2)

print(f'Each person should pay: {result}')

time.sleep(5) 
