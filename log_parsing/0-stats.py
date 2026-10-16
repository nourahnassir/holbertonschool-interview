#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        try:
            if len(parts) >= 2:
                # File size is always the last element
                file_size = int(parts[-1])
                total_size += file_size
                
                # Status code is the second to last element
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
        except (IndexError, ValueError):
            pass

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    raise

# Print final statistics if the loop finishes normally and not a multiple of 10
if line_count > 0:
    print_stats()
