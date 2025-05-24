import csv

def load_data(data, output_file):
    """
    Load data to a CSV file
    """
    if not data:
        return
    
    fieldnames = data[0].keys()
    
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Test loading
    from extract import extract_data
    from transform import transform_data
    
    data = extract_data('input_data.csv')
    transformed = transform_data(data)
    load_data(transformed, 'output_data.csv')
    print("Data loaded to output_data.csv")