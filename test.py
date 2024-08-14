from request_point import request_point

values_input = input("Enter values to search, space separated:")

values = [float(x) for x in values_input.split()]

print(f'Running for {values}')

for value in values:
    result, uncertainty = request_point('led_resistance_simple', value, 5)

# test = {
#     'supply_voltage': 11,
#     'current': 21e-3
# }

# result, uncertainty = request_point('led_resistance_complex', test, 10)

