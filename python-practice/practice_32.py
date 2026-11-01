jobs = [
    {"id": "job-201", "status": "failed", "attempts": 1},
    {"id": "job-202", "status": "completed", "attempts": 2},
    {"id": "job-203", "status": "failed", "attempts": 3},
    {"id": "job-204", "status": "pending", "attempts": 0},
    {"id": "job-205", "status": "failed", "attempts": 2},
    {"id": "job-206", "status": "completed", "attempts": 1},
]


def build_retry_plan(jobs, max_attempts):
    retry_job_ids = []
    exhausted_job_ids = []
    ignored_job_ids = []

    for job in jobs:
        status = job["status"]
        attempts = job["attempts"]
        job_id = job["id"]
        if status != "failed":
            ignored_job_ids.append(job_id)
        elif attempts < max_attempts:
            retry_job_ids.append(job_id)
        else:
            exhausted_job_ids.append(job_id)
    return {
        "retry_job_ids": retry_job_ids,
        "exhausted_job_ids": exhausted_job_ids,
        "ignored_job_ids": ignored_job_ids,
    }


print(build_retry_plan(jobs, 2))
