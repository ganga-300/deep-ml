import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    matrix = np.array(matrix)
    determinant = np.linalg.det(matrix)
    if determinant!=0:
        inverse = np.linalg.inv(matrix)
        return inverse
    return None