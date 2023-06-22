def calculate_bmi (user_weight_lb, user_height_ft, user_height_in):
    user_height = user_height_ft * 12 + user_height_in
    user_bmi = (user_weight_lb / (user_height * user_height)) * 703

    return user_bmi


user_weight = float(input("Enter your weight in pounds: "))
user_height_feet = int(input("Enter your height in feet: "))
user_height_inches = int(input("Enter the remaining height in inches: "))

user_bmi = calculate_bmi(user_weight, user_height_feet, user_height_inches)
user_bmi_rounded = round(user_bmi, 2)


print(f"\nYour BMI is {user_bmi_rounded}.")
if user_bmi < 18.5:
    bmi_category = "underweight"
elif user_bmi < 25:
    bmi_category = "normal weight"
elif user_bmi < 30:
    bmi_category = "overweight"
else:
    bmi_category = "obese"


print(f"Your BMI would be classified as falling within the {bmi_category} range.")

user_height_cm = (user_height_feet * 12 + user_height_inches) * 2.54
user_min_weight_kg = 18.5 * (user_height_cm * user_height_cm) / 10000
user_max_weight_kg = 24.9 * (user_height_cm * user_height_cm) / 10000
user_min_weight_lb = user_min_weight_kg * 2.20462
user_max_weight_lb = user_max_weight_kg * 2.20462

print(f"\nFor your height, a healthy weight range would be considered between {user_min_weight_lb:.2f} and {user_max_weight_lb:.2f} pounds.")