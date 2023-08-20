#!/usr/bin/python3

'''A script that reads stdin line by line and computes metrics.'''

import sys

# Initialize a dictionary to store status code counts
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize variables for total file size and line counter
total_size = 0
line_count = 0

try:
    # Read each line from stdin
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        # Check if the line format is valid
        if len(parts) == 9:
            status_code = parts[7]
            try:
                file_size = int(parts[8])

                # Update status code count if applicable
                if status_code in status_counts:
                    status_counts[status_code] += 1

                # Update total file size and line counter
                total_size += file_size
                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print('File size:', total_size)
                    for code, count in sorted(status_counts.items()):
                        if count != 0:
                            print(f'{code}: {count}')
                    print()

            except KeyboardInterrupt:
                # Print statistics and exit on keyboard interruption
                print('File size:', total_size)
                for code, count in sorted(status_counts.items()):
                    if count != 0:
                        print(f'{code}: {count}')
                sys.exit(0)
            except Exception:
                pass

except KeyboardInterrupt:
    # Print statistics and exit on keyboard interruption
    print('File size:', total_size)
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print(f'{code}: {count}')
    sys.exit(0)
