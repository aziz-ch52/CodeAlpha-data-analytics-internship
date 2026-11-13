import matplotlib.pyplot as plt
import seaborn as sns

# Force the visual style you prefer globally
sns.set_theme(style="darkgrid")


def plot_numerical_distribution(df, column):
    """Generates a histogram and KDE for a single numeric column."""
    if column in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], bins=50, kde=True)
        plt.title(f'Distribution of {column.capitalize()}')
        plt.show()


def plot_correlation_matrix(df):
    """Generates a heatmap of correlations between all numeric features."""
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True,
                    cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
        plt.title("Feature Correlation Matrix")
        plt.show()
    else:
        print("Not enough numerical columns to compute correlations.")
