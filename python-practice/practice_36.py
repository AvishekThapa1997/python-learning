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


def get_jobs_by_status(jobs, status):
    status = "unknown" if status is None else status
    return [
        job
        for job in jobs
        if ("unknown" if ((job_status := job.get("status")) is None) else job_status)
        == status
    ]


print(get_jobs_by_status(jobs, None))
