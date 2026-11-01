from collections import defaultdict

jobs = [
    {"id": "job-401", "status": "pending"},
    {"id": "job-402", "status": "failed"},
    {"id": "job-403", "status": "completed"},
    {"id": "job-404", "status": None},
    {"id": "job-405"},
    {"id": "job-406", "status": "failed"},
    {"id": "job-407", "status": "pending"},
    {"id": "job-408", "status": "completed"},
]


def group_jobs_by_status(jobs):
    job_groups = defaultdict(list)
    for job in jobs:
        job_status = job.get("status") or "unknown"
        job_groups[job_status].append(job)
    return dict(job_groups)


print(group_jobs_by_status(jobs))
