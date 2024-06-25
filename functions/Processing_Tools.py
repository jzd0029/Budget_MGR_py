# print the data frame
def print_all(data_frame):
    print("\nDataFrame:")
    print(data_frame)


# print the columns list in the DataFrame file type from Pandas
def print_columns_list(data_frame):
    # List the column names
    print("\nColumn names:")
    print(data_frame.columns.tolist())


# print a specific column in the DataFrame file type from Pandas
def print_column(data_frame, column_name):
    # Access a specific column
    print(f"\nContents of column '{column_name}':")
    print(data_frame[column_name])


# print a specific row in the DataFrame file type from Pandas
def print_row(data_frame, row_index):
    # Access a specific row by index
    print(f"\nContents of row at index {row_index}:")
    print(data_frame.iloc[row_index])
