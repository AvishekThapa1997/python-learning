from collections import defaultdict

jobs = [
    {"id": "job-301", "status": "completed"},
    {"id": "job-302", "status": "failed"},
    {"id": "job-301", "status": "retrying"},
    {"id": "job-303", "status": "pending"},
    {"id": "job-302", "status": "completed"},
    {"id": "job-301", "status": "completed"},
    {"id": "job-304", "status": "failed"},
    {"id": "job-304", "status": "retrying"},
]


def find_duplicate_jobs(jobs):
    job_frequency = defaultdict(int)
    for job in jobs:
        job_frequency[job["id"]] += 1
    duplicate_jobs = [job for job in jobs if job_frequency[job["id"]] > 1]
    return duplicate_jobs


print(find_duplicate_jobs(jobs))
