"""Analyze a web server access log and create a summary report.

Expected input: Common/Combined Log Format, for example:
127.0.0.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024
"""

import argparse
import re
from collections import Counter
from pathlib import Path

LOG_PATTERN = re.compile(
    r'^(?P<ip>\\S+)\\s+\\S+\\s+\\S+\\s+\\[[^\\]]+\\]\\s+'
    r'"(?P<request>[^"]*)"\\s+(?P<status>\\d{3})\\s+\\S+'
)


def parse_log_line(line):
    """Extract the IP address, endpoint, and status code from one log line."""
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    request_parts = match.group("request").split()
    endpoint = request_parts[1] if len(request_parts) >= 2 else "UNKNOWN"

    return {
        "ip": match.group("ip"),
        "endpoint": endpoint,
        "status": int(match.group("status")),
    }


def analyze_log_file(file_path):
    """Read the log and calculate request, error, IP, endpoint, and status counts."""
    total_requests = 0
    error_count = 0
    malformed_lines = 0
    ip_counts = Counter()
    endpoint_counts = Counter()
    status_counts = Counter()

    with Path(file_path).open("r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            if not line.strip():
                continue

            record = parse_log_line(line)
            if record is None:
                malformed_lines += 1
                continue

            total_requests += 1
            ip_counts[record["ip"]] += 1
            endpoint_counts[record["endpoint"]] += 1
            status_counts[record["status"]] += 1

            if record["status"] >= 400:
                error_count += 1

    return {
        "total_requests": total_requests,
        "error_count": error_count,
        "malformed_lines": malformed_lines,
        "ip_counts": ip_counts,
        "endpoint_counts": endpoint_counts,
        "status_counts": status_counts,
    }


def create_report(results, top_n=5):
    """Format the analysis results as a readable text report."""
    lines = [
        "LOG FILE ANALYSIS REPORT",
        "=" * 30,
        f"Total requests: {results['total_requests']}",
        f"Error responses (4xx and 5xx): {results['error_count']}",
        f"Malformed lines skipped: {results['malformed_lines']}",
        "",
        f"Top {top_n} IP addresses:",
    ]

    if results["ip_counts"]:
        lines.extend(
            f"{ip}: {count}"
            for ip, count in results["ip_counts"].most_common(top_n)
        )
    else:
        lines.append("No valid IP records found.")

    lines.extend(["", f"Top {top_n} requested endpoints:"])
    if results["endpoint_counts"]:
        lines.extend(
            f"{endpoint}: {count}"
            for endpoint, count in results["endpoint_counts"].most_common(top_n)
        )
    else:
        lines.append("No valid endpoint records found.")

    lines.extend(["", "HTTP status-code counts:"])
    if results["status_counts"]:
        lines.extend(
            f"{status}: {count}"
            for status, count in sorted(results["status_counts"].items())
        )
    else:
        lines.append("No valid status codes found.")

    return "\\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a server access log and summarize request activity."
    )
    parser.add_argument(
        "log_file",
        nargs="?",
        default="server.log",
        help="Input log file (default: server.log)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top IP addresses and endpoints to display (default: 5)",
    )
    parser.add_argument(
        "--output",
        default="analysis_report.txt",
        help="Output report filename (default: analysis_report.txt)",
    )
    args = parser.parse_args()

    if args.top < 1:
        parser.error("--top must be at least 1")

    log_path = Path(args.log_file)
    if not log_path.is_file():
        parser.error(f"Log file not found: {log_path}")

    try:
        results = analyze_log_file(log_path)
        report = create_report(results, args.top)
        print(report)
        Path(args.output).write_text(report + "\\n", encoding="utf-8")
        print(f"\\nReport saved to: {args.output}")
    except OSError as error:
        parser.error(f"Could not read or write a file: {error}")


if __name__ == "__main__":
    main()
