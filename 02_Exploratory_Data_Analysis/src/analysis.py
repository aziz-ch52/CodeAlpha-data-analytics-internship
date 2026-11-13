import pandas as pd

def engineer_features(df):
    """
    Generates new mathematical features required for final analysis.
    """
    if 'price' in df.columns and 'quantity' in df.columns:
        df['total_revenue'] = df['price'] * df['quantity']
    return df

def get_category_performance(df, category_col='category', revenue_col='total_revenue'):
    """
    Aggregates total revenue by category and returns a sorted series.
    """
    if category_col in df.columns and revenue_col in df.columns:
        return df.groupby(category_col)[revenue_col].sum().sort_values(ascending=False)
    return None
