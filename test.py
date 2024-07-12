from request_point import request_point

for i in [80, 130, 150]:
    result, uncertainty = request_point('led_resistance_simple', i, 5)

# test = {
#     'supply_voltage': 11,
#     'current': 21e-3
# }

# result, uncertainty = request_point('led_resistance_complex', test, 10)

