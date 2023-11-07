#výpočet BMI
# BMI = váha v kg / (výšky v m) na2

height = float(input("zadejte svou výšku v m:\n"))
weight = float(input("zadejte svou váhu v kg:\n"))

bmi = weight / height**2

print(round(bmi, 1))

if bmi < 18.5:
    print("Máte podváhu")
elif bmi < 24.9:
    print("Máte normální váhu")
elif bmi < 29.9:
    print("Máte nadváhu")
elif bmi < 34.9:
    print("máte obezitu")
else:
    print("máte těžkou obezitu")
