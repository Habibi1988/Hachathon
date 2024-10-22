import pandas as pd
import numpy as np

class DataPreprocessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load data from a CSV file."""
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def handle_missing_values(self):
        """Handle missing values in the dataset."""
        if self.data is not None:
            initial_len = len(self.data)
            self.data = self.data.dropna()  # Drop rows with any NaN values
            print(f"Missing values handled. Rows dropped: {initial_len - len(self.data)}")
        else:
            print("Data is not loaded. Please load the data first.")

    def remove_duplicates(self):
        """Remove duplicate rows in the dataset."""
        if self.data is not None:
            before_shape = self.data.shape
            self.data = self.data.drop_duplicates()  # Drop duplicate rows
            after_shape = self.data.shape
            print(f"Duplicates removed. Shape before: {before_shape}, Shape after: {after_shape}")
        else:
            print("Data is not loaded. Please load the data first.")

    def remove_outliers(self):
        """Remove outliers from numerical columns using the IQR method."""
        if self.data is not None:
            numeric_columns = self.data.select_dtypes(include=[np.number]).columns
            initial_shape = self.data.shape

            for column in numeric_columns:
                Q1 = self.data[column].quantile(0.25)
                Q3 = self.data[column].quantile(0.75)
                IQR = Q3 - Q1

                # Define outliers as points outside of 1.5 * IQR from Q1 or Q3
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                # Filter out the outliers
                self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]
            
            final_shape = self.data.shape
            print(f"Outliers removed. Shape before: {initial_shape}, Shape after: {final_shape}")
        else:
            print("Data is not loaded. Please load the data first.")

    def save_clean_data(self, output_file):
        """Save the cleaned data to a CSV file."""
        if self.data is not None:
            try:
                self.data.to_csv(output_file, index=False)
                print(f"Cleaned data saved to {output_file}")
            except Exception as e:
                print(f"Error saving data: {e}")
        else:
            print("Data is not loaded. Please load the data first.")

    def process(self):
        """Run the entire data preprocessing pipeline."""
        self.load_data()
        self.handle_missing_values()
        self.remove_duplicates()
        self.remove_outliers()

if __name__ == "__main__":
    # Define the file paths
    input_file = r'C:\Users\mhabi\Documents\Project for Hacatons\2023_accidents_causa-bcn.csv'
    output_file = r'C:\Users\mhabi\Documents\Project for Hacatons\cleaned_2023_accidents_causa-bcn.csv'

    # Create a DataPreprocessing object
    model = DataPreprocessing(input_file)

    # Run the data processing pipeline
    model.process()

    # Save the cleaned and processed data
    model.save_clean_data(output_file)
