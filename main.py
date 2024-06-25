import pandas as pd


def read_csv_file(csv_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path, skiprows=[0, 1, 2])
    return df


def main():
    csv_path = "Redstone_exports/June.csv"  # Replace with your CSV file path

    # Read and parse the CSV file
    df = read_csv_file(csv_path)

    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Access a specific column
    column_name = "Balance"  # Replace with the column name you want to access
    print(f"\nContents of column '{column_name}':")
    print(df[column_name])

    # Access a specific row by index
    row_index = 0  # Replace with the row index you want to access
    print(f"\nContents of row at index {row_index}:")
    print(df.iloc[row_index])


if __name__ == "__main__":
    main()
