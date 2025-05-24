def transform_data(data):
    """
    Simple transformation: convert names to uppercase and add a processed flag
    """
    transformed = []
    for record in data:
        transformed_record = {
            'name': record['name'].upper(),
            'age': int(record['age']),
            'email': record['email'].lower(),
            'processed': True
        }
        transformed.append(transformed_record)
    return transformed

if __name__ == "__main__":
    # Test transformation
    from extract import extract_data
    data = extract_data('input_data.csv')
    transformed = transform_data(data)
    print("Transformed data sample:", transformed[:1])