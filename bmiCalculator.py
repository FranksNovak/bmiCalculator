#výpočet BMI
# BMI = váha v kg / (výšky v m) na2
name = input("Zadejte své jméno\n")
height = float(input("zadejte svou výšku v m:\n"))
weight = float(input("zadejte svou váhu v kg:\n"))

bmi = weight / height**2

print(round(bmi, 1))

if bmi < 18.5:
    print(f"{name} Máte pdodváhu")
elif bmi < 24.9:
    print(f"{name} Máte normální váhu")
elif bmi < 29.9:
    print(f"{name} Máte nadváhu")
elif bmi < 34.9:
    print(f"{name} máte obezitu")
else:
    print(f"{name} máte těžkou obezitu")

print("kontrola")