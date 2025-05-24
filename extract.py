import csv

def extract_data(input_file):
    """
    Extract data from a CSV file
    """
    data = []
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    # Test extraction
    extracted_data = extract_data('input_data.csv')
    print("Extracted data sample:", extracted_data[:1])