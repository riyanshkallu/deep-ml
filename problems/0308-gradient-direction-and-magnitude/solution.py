import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here

	magnitude = 0
	for num in range(len(gradient)):
		magnitude += gradient[num] ** 2
	magnitude **= (1/2)

	if magnitude == 0:
		return {'magnitude': 0, 'direction': [0,0], 'descent_direction': [0,0]}
	
	direction = [num/magnitude for num in gradient]
	
	descent_direction = [-1*num for num in direction]

	return {'magnitude': magnitude, 'direction': direction, 'descent_direction': descent_direction}

	pass