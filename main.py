from functions.Import_Tools import *
from functions.Export_Tools import *
from functions.Processing_Tools import *

# def import_month_csv_file(csv_path):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_path, skiprows=[0, 1, 2])
#     return df


def main():
    import_csv_path = "Redstone_exports/June.csv"  # Replace with your CSV file path

    # Read and parse the CSV file
    df = import_rfcu_csv_file(import_csv_path, display_all=0, display_cols=0)

    # print a specific column
    # print_column(df, 'Balance')

    # Access a specific row by index
    # print_row(df, 0)

    # place each transaction in a group for the budget
    # TODO: group descriptions into major budget categories...
    df['Budget Group'] = df['Description']

    # Display the updated DataFrame
    print_all(df)

    # Write the updated DataFrame to a new CSV file
    export_csv_path = 'Processed/June.csv'  # Specify the path for the new CSV file
    export_processed_csv_file(df, export_csv_path)


if __name__ == "__main__":
    main()
