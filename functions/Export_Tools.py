# Write the DataFrame to a new CSV file
def export_processed_csv_file(data_frame, export_csv_path):
    data_frame.to_csv(export_csv_path, index=False)  # index=False to avoid writing row indices
    print(f"\nDataFrame written to {export_csv_path}")
