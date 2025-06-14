weight = float(input("Enter your body weight in kg : "))
height = float(input("Enter your height in meters : "))

bmi = weight / (height ** 2)
print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You have a Normal weight. Good job!")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight.")
else:
    print("You are Obese. Please consult a doctor.")