import pandas as pd

# --- Step 1: Create sample data ---
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 28],
    "city": ["New York", "London", "Paris"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# --- Step 2: Write to CSV ---
filename = "pandas/data.csv"
df.to_csv(filename, index=False)
print(f"Data written to {filename}\n")

# --- Step 3: Read the CSV file back ---
df_read = pd.read_csv(filename)
print("Read data from CSV:\n")
print(df_read)
