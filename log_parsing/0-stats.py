#!/usr/bin/python3
"""
Module 0-stats
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


if __name__ == "__main__":
    has_input = False
    try:
        for line in sys.stdin:
            has_input = True
            line_count += 1
            parts = line.split()

            try:
                if len(parts) >= 2:
                    file_size = int(parts[-1])
                    total_size += file_size

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

    if line_count > 0 or not has_input:
        print_stats()
