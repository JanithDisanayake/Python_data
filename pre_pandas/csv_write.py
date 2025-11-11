import csv

# File path
filename = "pre_pandas/data2.csv"

# --- Step 1: Write sample data into CSV file ---
sample_data = [
    ["name", "age", "city"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 28, "Paris"]
]

# Write data to CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

print(f"Sample data written to {filename}\n")

# --- Step 2: Read the CSV file back and print it ---
with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print("Header:", header)
    
    for row in reader:
        print(row)
