import os
import json

def count_valid_files(directory, dbi):
    total_count = 0
    valid_count = 0

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                data = json.load(f)
                if data['Decentralized_Business_Index'] == dbi:
                    total_count += 1
                    if data['valid']:
                        valid_count += 1

    return valid_count, total_count

directory = '/path/to/your/json/directory'  # replace with your directory
dbi = 'enter DBI here'  # replace with your DBI
valid, total = count_valid_files(directory, dbi)
print(f'Out of {total} files with the DBI of "{dbi}", {valid} were valid.')


def is_ratio_above_70_percent(valid_count, total_count):
    # Guard against division by zero
    if total_count == 0:
        return False

    # Calculate ratio and check if it's greater than 0.7 (70%)
    ratio = valid_count / total_count
    return ratio > 0.7