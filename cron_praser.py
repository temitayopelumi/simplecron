#!/usr/bin/env python3

import sys

def format_output(output):
    """Format the expanded cron fields for display."""
    lines = []
    for name, value in output.items():
        values = " ".join(str(v) for v in value) if isinstance(value, list) else str(value)
        lines.append(f"{name.ljust(14)} {values}")
    return "\n".join(lines)

def validate_range(start, end, min_value, max_value, part):
    if start < min_value or end > max_value:
        raise ValueError(f"Value {part} out of bounds ({min_value}-{max_value})")
    if start > end:
        raise ValueError(f"Invalid range {part} (start cannot be greater than end)")

def parse_field(field, min_value, max_value):
    values = []
    if field == '*':
        for i in range(min_value, max_value + 1):
            values.append(i)
        return values
    
    values = []
    for part in field.split(','):
        part = part.strip()
        if not part:
            raise ValueError("Empty field part found")
        if '/' in part:
            base, step = part.split('/')
            if step == "" or int(step) <= 0:
                raise ValueError("Step value cannot be empty, negative, or zero")
            step = int(step)
            if base == '*':
                start, end = min_value, max_value
            elif '-' in base:
                start, end = base.split('-')
                start, end = int(start), int(end)
            else:
                start = int(base)
                end = max_value
            validate_range(start, end, min_value, max_value, part)
            for value in range(start, end + 1, step):
                values.append(value)
        elif '-' in part:
            start, end = part.split('-')
            start, end = int(start), int(end)
            validate_range(start, end, min_value, max_value, part)
            for value in range(start, end + 1):
                values.append(value)
        else:
            val = int(part)
            if val < min_value or val > max_value:
                raise ValueError(f"Value {part} out of bounds ({min_value}-{max_value})")
            values.append(val)
    return sorted(set(values))

def parse_cron(line):
    parts = line.strip().split()
    if len(parts) < 6:
        raise ValueError("Cron line must have at least 6 fields")
    minute = parse_field(parts[0], 0, 59)
    hour = parse_field(parts[1], 0, 23)
    day_of_month = parse_field(parts[2], 1, 31)
    month = parse_field(parts[3], 1, 12)
    day_of_week = parse_field(parts[4], 0, 6)
    command = ' '.join(parts[5:])

    return {
        'minute': minute,
        'hour': hour,
        'day_of_month': day_of_month,
        'month': month,
        'day_of_week': day_of_week,
        'command': command
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: cron_parser.py <cron_line>")
        sys.exit(1)

    cron_line = sys.argv[1]
    try:
        output = parse_cron(cron_line)
        formatted_output = format_output(output)
        print("Parsed cron line:")
        print(formatted_output)
    except ValueError as e:
        print(f"Error parsing cron line: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

