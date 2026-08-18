def prune_weak_alpha_factors(factor_matrix, threshold=0.05):
    """Filters out low-performing quantitative factors within the Vibe-Trading pipeline."""
    filtered_matrix = factor_matrix[factor_matrix['alpha_score'] >= threshold]
    print(f"Pruned factors. Remaining active alphas: {len(filtered_matrix)}")
    return filtered_matrix
