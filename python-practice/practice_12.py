from collections import defaultdict
from datetime import datetime


def create_request_metadata(
    request_id: str,
    created_at: datetime | None = None,
):
    if created_at is None:
        created_at = datetime.now()
    return {
        "request_id": request_id,
        "created_at": created_at,
    }


first = create_request_metadata("req-101")
second = create_request_metadata("req-102")

print(first)
print(second)


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
        result[event["status"]].append(event["service"])
    return result


print(group_events_by_status(events))
