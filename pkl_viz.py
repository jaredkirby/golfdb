import pandas as pd

# Load the pickle file
data = pd.read_pickle("golfDB.pkl")

# Display the data
print(data)


# Save the data to a CSV file
data.to_csv("golfDB_2.csv")
