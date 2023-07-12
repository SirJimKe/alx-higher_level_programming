#!/usr/bin/python3
"""a script that reads stdin"""


def compute_metrics():
    """reads from standard input (sys.stdin) line by line"""
    total_file_size = 0
    status_code_counts = defaultdict(int)

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split(' ')
            file_size = int(parts[-1])
            status_code = parts[-2]
            total_file_size += file_size
            status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print("Total file size: {}".format(total_file_size))
                for code in sorted(status_code_counts.keys()):
                    print("{} : {}".format(code, status_code_counts[code]))

    except KeyboardInterrupt:
        print("Total file size: {}".format(total_file_size))
        for code in sorted(status_code_counts.keys()):
            print("{} : {}".format(code, status_code_counts[code]))


if __name__ == "__main__":
    import sys
    from collections import defaultdict
    compute_metrics()
