"""Analyze a web server access log and create a summary report.

Expected input: Common/Combined Log Format, for example:
127.0.0.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024
"""

"""
Task: Web Server Log Analyzer
Reads a sample log file and generates an analysis report.
"""

from collections import Counter
from pathlib import Path
import re

# Create sample log file automatically
log_data = """\
127.0.0.1 - - [09/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1024
192.168.1.1 - - [09/Nov/2026:10:01:00 +0000] "GET /about HTTP/1.1" 200 2048
127.0.0.1 - - [09/Nov/2026:10:02:00 +0000] "GET /login HTTP/1.1" 404 512
192.168.1.2 - - [09/Nov/2026:10:03:00 +0000] "POST /login HTTP/1.1" 200 1024
127.0.0.2 - - [09/Nov/2026:10:04:00 +0000] "GET /contact HTTP/1.1" 500 256
"""

Path("server.log").write_text(log_data)

def analyze_log():
    ip_counts = Counter()
    endpoint_counts = Counter()
    status_counts = Counter()

    total = 0
    errors = 0

    with open("server.log", "r") as file:
        for line in file:
            match = re.search(
                r'^(\S+).*?"\S+ (\S+) HTTP/[\d.]+" (\d{3})',
                line
            )

            if match:
                ip, endpoint, status = match.groups()

                ip_counts[ip] += 1
                endpoint_counts[endpoint] += 1
                status_counts[status] += 1

                total += 1

                if int(status) >= 400:
                    errors += 1

    print("\n===== WEB SERVER LOG REPORT =====")
    print("Total Requests:", total)
    print("Error Requests:", errors)

    print("\nIP Address Counts:")
    for ip, count in ip_counts.items():
        print(ip, ":", count)

    print("\nEndpoint Counts:")
    for endpoint, count in endpoint_counts.items():
        print(endpoint, ":", count)

    print("\nHTTP Status Codes:")
    for status, count in status_counts.items():
        print(status, ":", count)

    print("\n===== ANALYSIS COMPLETED =====")

    report = (
        f"Total Requests: {total}\n"
        f"Error Requests: {errors}\n"
        f"IP Addresses: {dict(ip_counts)}\n"
        f"Endpoints: {dict(endpoint_counts)}\n"
        f"Status Codes: {dict(status_counts)}"
    )

    Path("analysis_report.txt").write_text(report)

    print("\nReport saved as analysis_report.txt")


analyze_log()

