from collections import defaultdict

events = [
    {"service": "payments", "status": "success", "duration": 120},
    {"service": "auth", "status": "failure", "duration": 80},
    {"service": "payments", "status": "success", "duration": 150},
    {"service": "auth", "status": "success", "duration": 60},
    {"service": "payments", "status": "failure", "duration": 200},
]


def get_service_metrics(events):
    if not events:
        return {}
    event_summary_metrics = defaultdict(lambda : {
        "total_requests": 0,
        "successful": 0,
        "failed": 0,
        "total_duration": 0,
    })

    for event in events:
        service = event['service']
        is_success = event['status'] == "success"
        duration = event['duration']
        entry = event_summary_metrics[service]
        entry['total_requests'] += 1
        entry['total_duration'] += duration
        if is_success:
            entry['successful'] += 1
        else:
            entry['failed'] += 1
    for metric in event_summary_metrics.values():
        metric['average_duration'] = round(metric['total_duration'] / metric['total_requests'], 2)

    return dict(event_summary_metrics)


print(get_service_metrics(events))
