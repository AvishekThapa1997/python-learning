from collections import defaultdict

events = [
    {"service": "payments", "status": "success"},
    {"service": "auth", "status": "failure"},
    {"service": "payments", "status": "success"},
    {"service": "auth", "status": "success"},
    {"service": "payments", "status": "failure"},
    {"service": "notifications", "status": "success"},
]

def group_events_by_status(events):
    result = defaultdict(list)
    for event in events:
       result[event['status']].append(event['service'])
    return result #dict(result)

print(group_events_by_status(events))
