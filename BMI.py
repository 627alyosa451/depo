height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = weight / (height ** 2) 
result = round(float(BMI),2)
if float(result) < 18.5:
    print(f'your BMI is = {result} you are underweight')
elif 18.5 < float(result) < 25:
    print(f' your BMI is = {result} you are normalweight')
elif 25 < float(result) < 30:
    print(f' your BMI is = {result} you are slighty overweight')
elif 30 < float(result) < 35:
    print(f' your BMI is = {result} you are obese')
else:
    print(f' your BMI is = {result} you are clinically olbese')
    
