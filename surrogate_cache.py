# Third-party imports
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame as df
import pandas as pd

# Project imports
import twinlab as tl

# Import sudo-workflows
from calculate import led_resistance_simple, led_resistance_complex

API_KEY = 'oixh9y90xBedZnvV7_vbLA'

tl.set_api_key(API_KEY)

def active_train(new_datapoint, function_name):
	if function_name == "led_resistance_simple":
		new_resistance = led_resistance_simple(new_datapoint)

		# Convert to DataFrame
		new_data = df({"supply_voltage": [new_datapoint], "resistance": [new_resistance]})
	elif function_name == "led_resistance_complex":
		new_resistance = led_resistance_complex(new_datapoint['supply_voltage'], new_datapoint['current'])

		new_data = df({"supply_voltage": [new_datapoint['supply_voltage']], "current": [new_datapoint['current']], "resistance": [new_resistance]})
	else:
		print(f"Don't know what to do with {function_name} function")
		return

	# Add new data to model
	previous_data = tl.load_dataset(f"{function_name}.csv", verbose=True)
	df_train = pd.concat([previous_data, new_data], ignore_index=True)

	# Upload new training dataframe
	dataset_id = f"initial_{function_name}_train"
	dataset_upload = tl.Dataset(id=dataset_id)
	dataset_upload.upload(df_train, verbose=True)

	# Retrain model on added data
	emulator = tl.Emulator(id=function_name)
	if function_name == 'led_resistance_simple':
		emulator.train(dataset=dataset_upload, inputs=["supply_voltage"], outputs=["resistance"], verbose=True)
	elif function_name == 'led_resistance_complex':
		emulator.train(dataset=dataset_upload, inputs=["supply_voltage", "current"], outputs=["resistance"], verbose=True)

	df_train.to_csv(f"{function_name}.csv", encoding='utf-8', index=False)

	return

# def reccommend():
# 	return 

def initial_train(function_name):
	df_train = tl.load_dataset(f"{function_name}.csv", verbose=True)

	# Upload data
	dataset_id = f"initial_{function_name}_train"
	dataset_upload = tl.Dataset(id=dataset_id)
	dataset_upload.upload(df_train, verbose=True)

	# Train the emulator
	emulator = tl.Emulator(id=function_name)
	if function_name == 'led_resistance_simple':
		emulator.train(dataset=dataset_upload, inputs=["supply_voltage"], outputs=["resistance"], verbose=True)
	elif function_name == 'led_resistance_complex':
		emulator.train(dataset=dataset_upload, inputs=["supply_voltage", "current"], outputs=["resistance"], verbose=True)

	return

def predict(function_name, point):
	emulator = tl.Emulator(id=function_name)
	if function_name == 'led_resistance_simple':
		predict = df({"supply_voltage": [point]})
	elif function_name == 'led_resistance_complex':
		predict = df({"supply_voltage": [point['supply_voltage']], "current": [point['current']]})
	else:
		print(f"Don't know what to do with {function_name} function")
		return
	result, uncertainty = emulator.predict(predict)
	result = result.to_numpy()[0][0]
	uncertainty = uncertainty.to_numpy()[0][0]
	print(f'The result is {result} with uncertainty {uncertainty}.')
	return result, uncertainty

def plot_model(function_name):
	emulator = tl.Emulator(id=function_name)
	# Plot the results
	plt = emulator.plot(x_axis="supply_voltage", y_axis="resistance", x_lim=(0, 250))
	df_train = tl.load_dataset(f"{function_name}.csv", verbose=True)
	plt.scatter(df_train["supply_voltage"], df_train["resistance"], alpha=1, label="Training Data", color="black")
	plt.legend()
	plt.show()





