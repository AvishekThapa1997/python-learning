events = [
    {"id": 101, "status": "success"},
    {"id": 102, "status": "failed"},
    {"id": 103, "status": "failed"},
    {"id": 104, "status": "success"},
    {"id": 105, "status": "failed"},
]

def get_failed_event_ids(events):
    for event in events:
        if event['status'] == 'failed':
            yield event['id']

failed_event_ids = get_failed_event_ids(events) 

print(sum(failed_event_ids))
for failed_event_id in failed_event_ids:
    print(failed_event_id)
