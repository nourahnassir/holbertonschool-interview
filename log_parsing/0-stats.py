#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys


def print_statistics(total_size, status_codes):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                    total_size += file_size
                except ValueError:
                    pass

                try:
                    status_code = int(parts[-2])
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                except ValueError:
                    pass

            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
