reports = [
    {"id": 101, "duration": 250},
    {"id": 102, "duration": 800},
    {"id": 103, "duration": 900},
    {"id": 104, "duration": 200},
    {"id": 105, "duration": 1200},
]

def calculate_processing_cost(duration):
    # Assume this is an expensive calculation.
    return duration * 0.75

report_with_high_processing_cost = {
    report['id'] : processing_cost
    for report in reports
    if (processing_cost := calculate_processing_cost(report['duration'])) >= 600
}

print(report_with_high_processing_cost)
