from collections import defaultdict

events = [
    {"service": "payments", "status": "success"},
    {"service": "auth", "status": "failure"},
    {"service": "payments", "status": "success"},
    {"service": "auth", "status": "success"},
    {"service": "payments", "status": "failure"},
    {"service": "notifications", "status": "success"},
]

def count_events_by_status(events):
    result = defaultdict(int)
    for event in events:
        result[event['status']] += 1
    return result

print(count_events_by_status(events))


