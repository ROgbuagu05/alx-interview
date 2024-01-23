#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""


import sys

# Initialize dictionaries to store metrics
status_codes = {}
file_sizes = {}

# Read input from stdin line by line
for line in sys.stdin:
    # Ignore empty lines
    if not line.strip():
        continue

    parts = line.split()
    ip_address = parts[0]
    date = parts[1]
    request = parts[3]
    status_code = parts[4]
    file_size = parts[5]

    # Skip lines that don't match the expected format
    if not all([part.strip() for part in parts]):
        continue

    # Update metrics
    if status_code not in status_codes:
        status_codes[status_code] = 0
    status_codes[status_code] += 1

    if file_size:
        file_sizes[file_size] = file_sizes.get(file_size, 0) + 1

    # Print metrics every 10 lines or on keyboard interruption
    if len(sys.stdin.readline()) % 10 == 0 or sys.stdin.isatty() and sys.stdin.readline().startswith('Ctrl-C'):
        print('Total file size:', sum(file_sizes.values()))
        print('Number of lines by status code:')
        for status_code, count in sorted(status_codes.items()):
            print(f'{status_code}: {count}')
        print()

# Print final metrics
print('Total file size:', sum(file_sizes.values()))
print('Number of lines by status code:')
for status_code, count in sorted(status_codes.items()):
    print(f'{status_code}: {count}')
