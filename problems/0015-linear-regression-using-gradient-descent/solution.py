import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n), including a bias column of ones.
        y: Target vector of shape (m,).
        alpha: Learning rate.
        iterations: Number of gradient descent iterations.

    Returns:
        Learned weights as a 1D NumPy array of shape (n,).
    """
    m, n = X.shape
    y = y.reshape(-1, 1)
    theta = np.zeros((n, 1))

    for _ in range(iterations):
        predictions = X @ theta
        errors = predictions - y
        gradient = (X.T @ errors) / m
        theta = theta - alpha * gradient

    return theta.flatten()