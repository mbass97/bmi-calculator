# expanded code
# rawUserInput = input("please enter your body weight(kg):\t")
# userWeight = float(rawUserInput)

# rawUserInput = input("Please enter your height(cm):\t")
# userHeight = float(rawUserInput)

# def calculateBmi(weight, height):
#     bmi = height ** 2
#     bmi = weight / bmi
#     bmi *= 10_000
#     return bmi

# userBmi = calculateBmi(userWeight, userHeight)

# output = "Your BMI is: " + userBmi
# print(output)

# simplified code
userWeight = float(input("please enter your body weight(kg):\t"))
userHeight = float(input("Please enter your height(cm):\t"))

def calculateBmi(weight, height):
    bmi = (weight/(height**2)) * 10_000
    return bmi

userBmi = calculateBmi(userWeight, userHeight)

print(f'your BMI is: {userBmi}')