from collections import defaultdict

metrices = [
    {"service": "payments", "duration": 120},
    {"service": "auth", "duration": 80},
    {"service": "payments", "duration": 150},
    {"service": "auth", "duration": 60},
    {"service": "payments", "duration": 200},
]

def calculate_average_duration(metrices):
    if not metrices:
        return {}
    service_total_durations = defaultdict(list)
    for metrice in metrices:
        service_total_durations[metrice['service']].append(metrice['duration'])

    return {
        key:round(sum(durations)/ len(durations), 2)
        for key, durations in service_total_durations.items()
    }


print(calculate_average_duration(metrices))
    
    