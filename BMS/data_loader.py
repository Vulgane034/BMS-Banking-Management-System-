import pandas as pd
import os

def load_beac_data(file_path='data/CEMAC_2025.xls'):
    """
    Loads and parses BEAC monetary statistics from an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        pandas.DataFrame: A DataFrame containing the parsed data.
    """
    try:
        # Read the 'BEAC' sheet, using row 3 as the header
        df = pd.read_excel(file_path, sheet_name='BEAC', header=3)

        # Clean up column names
        df.columns = df.columns.str.strip()

        # Drop the first row which is empty
        df = df.drop(0)

        # Rename the first column for clarity
        df = df.rename(columns={'Fin de périodes                ACTIF': 'Period'})

        # Drop columns that are entirely NaN
        df = df.dropna(axis=1, how='all')

        # Forward fill NaNs in the 'Period' column
        df['Period'] = df['Period'].fillna(method='ffill')

        # Drop rows where all data columns (except 'Period') are NaN
        data_columns = [col for col in df.columns if col != 'Period']
        df = df.dropna(subset=data_columns, how='all')

        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    data = load_beac_data()
    if data is not None:
        print("Successfully loaded and cleaned BEAC data:")
        print(data.head())
        print("\nDataFrame Info:")
        data.info()
