from surrogate_cache import *
from calculate import *
import numpy as np
import pandas as pd

def request_point(function_name, point, tolerance):
	result, uncertainty = predict(function_name, point)

	percent_uncertainty = (uncertainty / result) * 100
	print(f'Pergentage uncertainty is : {percent_uncertainty}')
	if percent_uncertainty > tolerance:
		active_train(point, function_name)
		result, uncertainty = predict(function_name, point)


	return result, uncertainty