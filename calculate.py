def led_resistance_simple(supply_voltage):
	current = 20e-3 # 20mA
	led_voltage = 2 # 2V
	resistance = (supply_voltage - led_voltage) / current
	if resistance < 0:
		resistance = 0
	return resistance

def led_resistance_complex(supply_voltage, current):
	led_voltage = 2
	resistance = (supply_voltage - led_voltage) / current
	print(resistance)
	if resistance < 0:	
		resistance = 0
	return resistance