import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	S = np.array(S)
	T = np.array(T)

	detT = np.linalg.det(T)
	detS = np.linalg.det(S)
	if detT!=0 and detS!=0:
		
		invT = np.linalg.inv(T)
		
		res = invT @ A @ S
		return res.tolist()
	return -1


