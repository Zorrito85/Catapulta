def load_config(file_path):
    # Load configuration from a file
    with open(file_path, 'r') as file:
        config = file.read()
    return config

def save_results(file_path, results):
    # Save results to a file
    with open(file_path, 'w') as file:
        file.write(results)