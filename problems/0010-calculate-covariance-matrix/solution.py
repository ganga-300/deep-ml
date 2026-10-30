def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    
    # Step 1: Calculate the mean for each feature
    means = [sum(feature) / n_observations for feature in vectors]
    
    # Step 2: Initialize the covariance matrix with zeros
    cov_matrix = [[0.0] * n_features for _ in range(n_features)]
    
    # Step 3: Compute covariance for each pair of features
    for i in range(n_features):
        for j in range(n_features):
            total = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n_observations)
            )
            cov_matrix[i][j] = total / (n_observations - 1)
            
    return cov_matrix