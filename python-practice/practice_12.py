from datetime import datetime


def create_request_metadata(request_id: str, created_at: datetime | None = None):
    if created_at is None:
        created_at = datetime.now()
    return {
        "request_id" : request_id,
        "created_at" : created_at
    }    



first = create_request_metadata("req-101")
second = create_request_metadata("req-102")


print(first)
print(second)

# Each request should receive its own creation timestamp.