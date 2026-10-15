activities = [
    (104, "Ravi", 12),
    (101, "Amit", 25),
    (103, "Neha", 18),
    (102, "Priya", 7),
]

def generate_activity_report(activities):
    activity_report = [
        {
            "user_id":user_id,
            "username": user_name,
            "activity_count":activity_count,
            "status": "high" if activity_count >= 15 else "low"
        } 
        for user_id,user_name,activity_count in activities
        if user_name and activity_count >= 0
    ]
    activity_report.sort(key=lambda report : report['activity_count'],reverse=True)
    return activity_report

print(generate_activity_report(activities))