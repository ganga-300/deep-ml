import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	
	eigen = np.linalg.eigvals(matrix).tolist()
	return eigen