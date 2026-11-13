import pandas as pd

def clean_ecommerce_data(df):
    """
    Executes the standard deduplication and null-handling pipeline.
    """
    # Strip exact duplicates
    df_clean = df.drop_duplicates().copy()
    
    # Standardize column names (lowercase, underscores)
    df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_')
    
    # Handle basic nulls logically
    for col in df_clean.columns:
        if df_clean[col].dtype in ['int64', 'float64']:
            # Median imputation for continuous variables to avoid skew
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        else:
            # Placeholder for missing categorical data
            df_clean[col] = df_clean[col].fillna('Unknown')
            
    # Standardize dates if the column exists
    if 'transaction_date' in df_clean.columns:
        df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'], errors='coerce')
        
    return df_clean
