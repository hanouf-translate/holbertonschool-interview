#!/usr/bin/python3
import re
import sys

LOG_PATTERN = re.compile(r'^\S+ - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')
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
            line = line.strip()
            match = LOG_PATTERN.match(line)

            if not match:
                continue

            status_code, file_size = match.groups()

            
            if status_code not in VALID_STATUS_CODES:
                continue

           
            try:
                total_size += int(file_size)
            except ValueError:
                continue

            status_counts[status_code] += 1
            line_count += 1

            
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    
    print_stats(total_size, status_counts)