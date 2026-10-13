#!/usr/bin/python3
"""Script that reads stdin line by line and computes log metrics."""
import sys

VALID_STATUS_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}

def print_stats(total_size, status_counts):
    """Prints the total accumulated file size and non-zero status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(VALID_STATUS_CODES, key=int):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {code: 0 for code in VALID_STATUS_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()

            if len(parts) < 2:
                continue

            file_size_str = parts[-1]
            status_code = parts[-2]

            try:
                file_size = int(file_size_str)
            except ValueError:
                continue

            if status_code in VALID_STATUS_CODES:
                status_counts[status_code] += 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    else:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()