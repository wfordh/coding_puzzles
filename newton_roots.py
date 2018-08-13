import numpy as np

def newton_sqrt(init_num, x0, err = 0.0001):
	"""
	Simple square root finding algorithm.
	:init_num: Integer to find the square root of
	:x0: Initial guess at square root
	:err: error threshold
	"""
	while np.abs(x0**2 - init_num) > err:
		x0 = x0 - (x0**2 - init_num)/(2*x0)
	
	return x0

def newton_cube_rt(init_num, x0, err = 0.0001):
	"""
	Simple cube root finding algorithm.
	:init_num: Integer to find the cube root of
	:x0: Initial guess at cube root
	:err: error threshold
	"""
	while np.abs(x0**3 - init_num) > err:
		x0 = x0 - (x0**3 - init_num)/(3*x0**2)
	
	return x0

## to do: write more general versions?