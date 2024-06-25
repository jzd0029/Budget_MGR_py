import pandas as pd
from functions.Processing_Tools import *


# import the transactions file exported from Redstone FCU
def import_rfcu_csv_file(csv_path, display_all, display_cols):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path, skiprows=[0, 1, 2])

    # Remove the 'Transaction Number' column
    df = df.drop(columns=['Transaction Number'])

    # Display the DataFrame
    if display_all == 1:
        print_all(df)

    if display_cols == 1:
        print_columns_list(df)

    return df

