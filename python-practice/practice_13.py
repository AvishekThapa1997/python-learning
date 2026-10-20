from datetime import datetime


def log_api_request(
    request_id: str,
    endpoint: str,
    timestamp:datetime | None = None,
):
    if timestamp is None:
        timestamp = datetime.now()
    return {
        "request_id": request_id,
        "endpoint": endpoint,
        "timestamp": timestamp,
    }


print(log_api_request("req-101", "/users"))
print(log_api_request("req-102", "/orders"))


def get_service_metrics():
    return {
        "total_requests": 120,
        "successful": 105,
        "failed": 10,
        "retries": 3,
        "timeouts": 2,
    }


print(type(get_service_metrics()))
