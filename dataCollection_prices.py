import pandas as pd
import numpy as np


# Function to read data from CSV and create DataFrame
def create_dataframe(csv_file):
    # Read CSV into DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    print("Column names from CSV:", df.columns)

    # Rename columns
    df.columns = ["day", "timestamp", "product", "bid_price_1", "bid_volume_1",
                  "bid_price_2", "bid_volume_2", "bid_price_3", "bid_volume_3",
                  "ask_price_1", "ask_volume_1", "ask_price_2", "ask_volume_2",
                  "ask_price_3", "ask_volume_3", "mid_price", "profit_and_loss"]

    return df


# Example usage
if __name__ == "__main__":
    # Replace 'file.csv' with the path to your CSV file
    csv_file = 'round-1-island-data-bottle/prices_round_1_day_0.csv'
    dataframe = create_dataframe(csv_file)
    print(dataframe.head(100))

    # Filter rows where product is "AMETHYSTS" and get corresponding mid_price values
    amethysts_mid_prices = dataframe.loc[dataframe['product'] == 'AMETHYSTS', 'mid_price'].tolist()
    starfruit_mid_prices = dataframe.loc[dataframe['product'] == 'STARFRUIT', 'mid_price'].tolist()

    '''
    # Print the list of mid_prices for AMETHYSTS
    print("Mid prices for product 'AMETHYSTS':", amethysts_mid_prices)
    
    '''
    # Calculate the average of mid_prices
    average_mid_price = sum(amethysts_mid_prices) / len(amethysts_mid_prices)

    # Print the average
    print("Average mid price for product 'AMETHYSTS':", average_mid_price)

    # Calculate the VWAP mid_price

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    amethysts_data = dataframe[dataframe['product'] == 'AMETHYSTS'][['bid_price_1', 'bid_volume_1']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    amethysts_data = amethysts_data.dropna(subset=['bid_price_1', 'bid_volume_1'])

    # Calculate the weighted sum and total volumes
    bid_1_weighted_sum = (amethysts_data['bid_price_1'] * amethysts_data['bid_volume_1']).sum()
    bid_1_volumes = amethysts_data['bid_volume_1'].sum()

    # Calculate VWAP_bid_2
    if bid_1_volumes != 0:
        vwap_bid_1 = bid_1_weighted_sum / bid_1_volumes
    else:
        vwap_bid_1 = np.nan

    # Print the dictionary
    print("Average Bid 1 VWAP price for product 'AMETHYSTS':", vwap_bid_1)

    # Calculate the VWAP mid_price

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    amethysts_data = dataframe[dataframe['product'] == 'AMETHYSTS'][['bid_price_2', 'bid_volume_2']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    amethysts_data = amethysts_data.dropna(subset=['bid_price_2', 'bid_volume_2'])

    # Calculate the weighted sum and total volumes
    bid_2_weighted_sum = (amethysts_data['bid_price_2'] * amethysts_data['bid_volume_2']).sum()
    bid_2_volumes = amethysts_data['bid_volume_2'].sum()

    # Calculate VWAP_bid_2
    if bid_2_volumes != 0:
        vwap_bid_2 = bid_2_weighted_sum / bid_2_volumes
    else:
        vwap_bid_2 = np.nan

    # Print the dictionary
    print("Average Bid 2 VWAP price for product 'AMETHYSTS':", vwap_bid_2)

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    amethysts_data = dataframe[dataframe['product'] == 'AMETHYSTS'][['bid_price_3', 'bid_volume_3']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    amethysts_data = amethysts_data.dropna(subset=['bid_price_3', 'bid_volume_3'])

    # Calculate the weighted sum and total volumes
    bid_3_weighted_sum = (amethysts_data['bid_price_3'] * amethysts_data['bid_volume_3']).sum()
    bid_3_volumes = amethysts_data['bid_volume_3'].sum()

    # Calculate VWAP_bid_2
    if bid_3_volumes != 0:
        vwap_bid_3 = bid_3_weighted_sum / bid_3_volumes
    else:
        vwap_bid_3 = np.nan

    # Print the dictionary
    print("Average Bid 3 VWAP price for product 'AMETHYSTS':", vwap_bid_3)

    # Filter rows where product is "AMETHYSTS" and get corresponding mid_price values
    amethysts_mid_prices = dataframe.loc[dataframe['product'] == 'AMETHYSTS', 'mid_price'].tolist()

    '''
    # Print the list of mid_prices for STARFRUIT
    print("Mid prices for product 'STARFRUIT':", starfruit_mid_prices)

    '''
    # Calculate the average of mid_prices
    average_starfruit_mid_price = sum(starfruit_mid_prices) / len(starfruit_mid_prices)

    # Print the average
    print("Average mid price for product 'STARFRUIT':", average_starfruit_mid_price)

    # Calculate the VWAP mid_price

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    starfruit_data = dataframe[dataframe['product'] == 'STARFRUIT'][['bid_price_1', 'bid_volume_1']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    starfruit_data = starfruit_data.dropna(subset=['bid_price_1', 'bid_volume_1'])

    # Calculate the weighted sum and total volumes
    star_bid_1_weighted_sum = (starfruit_data['bid_price_1'] * starfruit_data['bid_volume_1']).sum()
    star_bid_1_volumes = starfruit_data['bid_volume_1'].sum()

    # Calculate VWAP_bid_2
    if star_bid_1_volumes != 0:
        star_vwap_bid_1 = star_bid_1_weighted_sum / star_bid_1_volumes
    else:
        star_vwap_bid_1 = np.nan

    # Print the dictionary
    print("Average Bid 1 VWAP price for product 'STARFRUIT':", star_vwap_bid_1)

    # Calculate the VWAP mid_price

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    starfruit_data = dataframe[dataframe['product'] == 'STARFRUIT'][['bid_price_2', 'bid_volume_2']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    starfruit_data = starfruit_data.dropna(subset=['bid_price_2', 'bid_volume_2'])

    # Calculate the weighted sum and total volumes
    star_bid_2_weighted_sum = (starfruit_data['bid_price_2'] * starfruit_data['bid_volume_2']).sum()
    star_bid_2_volumes = starfruit_data['bid_volume_2'].sum()

    # Calculate VWAP_bid_2
    if star_bid_2_volumes != 0:
        star_vwap_bid_2 = star_bid_2_weighted_sum / star_bid_2_volumes
    else:
        star_vwap_bid_2 = np.nan

    # Print the dictionary
    print("Average Bid 2 VWAP price for product 'STARFRUIT':", star_vwap_bid_2)

    # Assuming 'dataframe' contains the DataFrame with your data
    # Filter rows where product is "AMETHYSTS" and extract bid_price_2 and bid_volume_2
    starfruit_data = dataframe[dataframe['product'] == 'STARFRUIT'][['bid_price_3', 'bid_volume_3']]

    # Drop rows with null values in bid_price_2 or bid_volume_2
    starfruit_data = starfruit_data.dropna(subset=['bid_price_3', 'bid_volume_3'])

    # Calculate the weighted sum and total volumes
    star_bid_3_weighted_sum = (starfruit_data['bid_price_3'] * starfruit_data['bid_volume_3']).sum()
    star_bid_3_volumes = starfruit_data['bid_volume_3'].sum()

    # Calculate VWAP_bid_2
    if star_bid_3_volumes != 0:
        star_vwap_bid_3 = star_bid_3_weighted_sum / star_bid_3_volumes
    else:
        star_vwap_bid_3 = np.nan

    # Print the dictionary
    print("Average Bid 3 VWAP price for product 'STARFRUIT':", star_vwap_bid_3)


