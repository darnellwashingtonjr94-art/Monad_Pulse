def compute_ic_series(alpha_factors, returns):
    """Calculates Information Coefficient (IC) series for Vibe-Trading quant factor research."""
    import pandas as pd
    df = pd.DataFrame({'factor': alpha_factors, 'return': returns})
    return df['factor'].corr(df['return'])
