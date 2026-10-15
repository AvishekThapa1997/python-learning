from functools import reduce

events = [
    {"service": "payments", "status": "success", "duration": 120},
    {"service": "auth", "status": "failure", "duration": 80},
    {"service": "payments", "status": "success", "duration": 150},
    {"service": "auth", "status": "success", "duration": 60},
    {"service": "payments", "status": "failure", "duration": 200},
    {"service": "auth", "status": "failure", "duration": 100},
]

def generate_event_summary(events):
    result = {}
    for event in events:
        entry = result.setdefault(event['service'],{
            "total_events":0,
            "success_count":0,
            "failure_count":0,
            "total_duration":0
        })
        is_success = event["status"] == "success"
        entry["total_events"] += 1
        entry["total_duration"] += event.get("duration", 0)
        if is_success:
            entry["success_count"] += 1
        else:
            entry["failure_count"] += 1
    return result



print(generate_event_summary(events))
