import csv

# Path to your CSV file
filename = "pre_pandas/data.csv"

# Open and read the CSV file
with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Optionally, read the header
    header = next(reader)  # Comment this line if your CSV has no header
    print("Header:", header)

    # Read the remaining rows
    for row in reader:
        print(row)
