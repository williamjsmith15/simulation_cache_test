from calculate import led_resistance_complex
import numpy as np
from pandas import DataFrame as df
import pandas as pd

voltages = np.linspace(0, 10, 11)
currents = np.linspace(10e-3, 20e-3, 11)

array = []

for volt in voltages:                                                  
	for curr in currents:
		# train = df({"supply_voltage": [volt], "current": [curr], "resistance": [led_resistance_complex(volt, curr)]})
		# training = pd.concat([training, train], ingnore_index=True)    
		array.append([volt, curr, led_resistance_complex(volt, curr)])

training = df(array, columns=['supply_voltage', 'current', 'resistance'])
training.to_csv('led_resistance_complex.csv', encoding='utf-8', index=False)

print(training)