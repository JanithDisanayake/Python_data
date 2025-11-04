# Simple Python script to read from a plain text file

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read the entire contents of the file
            contents = file.read()
            print("File contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    read_file("file.txt")
