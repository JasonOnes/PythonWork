"""
Second Attempt
"""


def distcon():
    """
    meter_ft = float(int(amount)) * 3.28084
    meter_km = int(amount) * 1000
    meter_mi = int(amount) * 0.000621371
    """

    amount = int(input("How far?: "))
    input_from = input("what unit of measure? ")
    input_to = input("what unit to convert to? ")
    meter_ft = float(amount) * 3.28084
    meter_km = amount * 1000
    meter_mi = amount * .000621371

    if input_from == "mi":
        return amount == amount * meter_mi
    elif input_from == "m":
        return amount
    elif input_from == "km":
        return amount == amount * meter_km
    elif input_from == "ft":
        return amount == amount * meter_ft

    if input_to == "mi":
        return output == meter_mi / amount
    elif input_to == "m":
        return output == amount
    elif input_to == "km":
        return output == meter_km / amount
    elif input_to == "ft":
        return output == meter_ft / amount

    print("{} {} is {} in {}.".format(amount, input_from, output, input_to))

distcon()
