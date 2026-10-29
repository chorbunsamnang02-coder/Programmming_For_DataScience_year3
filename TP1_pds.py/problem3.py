#Problem 3. Temperature Converter
# a / Use a for loop with range(0, 101, 20) to print the conversion table below
def celsius_to_fraen(cel , round_to=1):
    farenheit= cel *(9/5) +32
    return farenheit
print(celsius_to_fraen(7))

def fren_to_cel(far ,round_to=1):
    cel= (far-32)*5/9
    return cel
print(fren_to_cel(98.6))