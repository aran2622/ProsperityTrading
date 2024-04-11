import pandas as pd


# Function to read data from CSV and create DataFrame
def create_dataframe(csv_file):
    # Read CSV into DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    print("Column names from CSV:", df.columns)

    # Rename columns
    df.columns = ["timestamp", "buyer", "seller", "symbol",
                  "currency", "price", "quantity"]

    return df


# Example usage
if __name__ == "__main__":
    # Replace 'file.csv' with the path to your CSV file
    csv_file = 'round-1-island-data-bottle/trades_round_1_day_0_nn.csv'
    dataframe = create_dataframe(csv_file)
    print(dataframe.head())
