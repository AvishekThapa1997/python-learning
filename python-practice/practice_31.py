from collections import defaultdict
from typing import Literal, TypedDict


class Job(TypedDict):
    id: str
    type: Literal["email", "report"]
    status: Literal["completed", "failed", "pending", "unknown", "retrying"] = "unknown"


class JobSummary(TypedDict):
    total: int
    by_status: dict[str, int]
    failed_jobs: list[str]


jobs: list[Job] = [
    {"id": "job-101", "type": "email", "status": "completed"},
    {"id": "job-102", "type": "report", "status": "failed"},
    {"id": "job-103", "type": "email", "status": "pending"},
    {"id": "job-104", "type": "report", "status": "failed"},
    {"id": "job-105", "type": "email"},
    {"id": "job-106", "type": "report", "status": "completed"},
    {"id": "job-107", "type": "email", "status": "retrying"},
]


def summarize_jobs(jobs: list[Job]) -> JobSummary:
    by_status: defaultdict[str, int] = defaultdict(int)
    failed_jobs: list[str] = []
    for job in jobs:
        status = job.get("status", "unknown")
        if status == "failed":
            failed_jobs.append(job["id"])
        by_status[status] += 1
    return {
        "total": len(jobs),
        "by_status": dict(by_status),
        "failed_jobs": failed_jobs,
    }


print(summarize_jobs(jobs))
