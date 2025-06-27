try:
    number = float(input('Enter a number to convert: '))  # allows decimal input too

    def km_to_m():
        print(f"{number} km = {number * 1000} m")

    def mile_to_km():
        print(f"{number} miles = {number * 1.60934} km")

    def inch_to_cm():
        print(f"{number} inches = {number * 2.54} cm")

    def feet_to_inch():
        print(f"{number} feet = {number * 12} inches")

    def inch_to_feet():
        print(f"{number} inches = {number / 12:.2f} feet")

    def c_to_f():
        print(f"{number} °C = {(number * 9 / 5) + 32:.2f} °F")

    def f_to_c():
        print(f"{number} °F = {(number - 32) * 5 / 9:.2f} °C")

    def c_to_k():
        print(f"{number} °C = {number + 273.15} K")

    user_choice = input('Convert type (e.g., km_to_m, c_to_f): ').lower()

    dictionary = {
        'km_to_m': km_to_m,
        'mile_to_km': mile_to_km,
        'inch_to_cm': inch_to_cm,
        'feet_to_inch': feet_to_inch,
        'inch_to_feet': inch_to_feet,
        'f_to_c': f_to_c,
        'c_to_f': c_to_f,
        'c_to_k': c_to_k
    }

    conversion_function = dictionary.get(user_choice)

    if conversion_function:
        conversion_function()
    else:
        print("Invalid conversion type. Try: km_to_m, c_to_f, mile_to_km, etc.")

except ValueError:
    print('Invalid input. Please enter a valid number.')
