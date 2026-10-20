from typing import Any

reports: list[dict[str, Any]]= [
    {
        "id": 1,
        "service": "payments",
        "duration": 250,
        "status": "success",
    },
    {
        "id": 2,
        "service": "orders",
        "duration": 800,
        "status": "failed",
    },
    {
        "id": 3,
        "service": "payments",
        "duration": 900,
        "status": "failed",
    },
    {
        "id": 4,
        "service": "orders",
        "duration": 200,
        "status": "success",
    },
]

slow_report_ids = [
    report
    for report in reports
    if report['duration'] >= 500
]

failed_report_ids = [
    report
    for report in reports
    if report['status'] == "failed"
    and report['duration'] >= 500
]

complex_report_ids = []

for report in reports:
    if report['status'] == "failed" and report['duration'] >= 500 and report['service'] == "payments":
        complex_report_ids.append(report)