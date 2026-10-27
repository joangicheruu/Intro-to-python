# bmi calc
# • Underweight: Below 18.5
# • Healthy Weight: 18.5 to 24.9
# • Overweight: 25.0 to 29.9
# • Obesity (Class I): 30.0 to 34.9
# • Obesity (Class II): 35.0 to 39.9
# • Severe Obesity (Class III): 40.0 or higher

weight = input("please enter your weight in kilos: ")
height = int(input("please enter your height in meters: "))

w = float(weight)
h= float(height)

bmi = w/(h**2)
# age ==19
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("you are healthy")
elif bmi >= 25.0 and bmi <= 29.9:
    print("you are overweight")
elif bmi >= 30.0 and bmi <= 34.9:
    print("you are obese class 1")
elif bmi >= 35.0 and bmi <= 39.9:
    print("you are obese class 2")
else:
    print("you are obese class 3")

# git init
# git add .(don't include the virtual environment)

# git commit -m ""
#