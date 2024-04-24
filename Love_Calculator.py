name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
double = name1 + name2
lower_case = double.lower()
t = double.count('t')
r = double.count('r')
u = double.count('u')
e = double.count('e')
true_total = t + r + u + e

l = double.count('l')
o = double.count('o')
v = double.count('v')
e = double.count('e')
love_total = l + o + v + e

result = str(true_total) + str(love_total)
if int(result) < 10 or int(result) > 90:
    print(f'your score is {result}, you go together like coke and mentos.')
elif 40 < int(result) < 50:
    print(f'your score is {result}, you are alright together.')
else:
    print(f'your score is {result}.')

