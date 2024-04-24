age = input("What is your current age? ")
left = 90 - int(age)
left_mounth = int(left) * 12
left_week = int(left) * 52
left_day = int(left) * 365
print(f'You have {left} years, {left_mounth} months, {left_week} weeks, {left_day} days left.'  )
