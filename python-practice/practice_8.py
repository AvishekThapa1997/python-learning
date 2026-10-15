projects = [
    {"name": "Payments", "priority": "high", "overdue_days": 3},
    {"name": "Dashboard", "priority": "low", "overdue_days": 10},
    {"name": "Authentication", "priority": "high", "overdue_days": 1},
    {"name": "Notifications", "priority": "medium", "overdue_days": 5},
    {"name": "Analytics", "priority": "medium", "overdue_days": 2},
]


def generate_project_report(projects:list):
    priority = {
        "high" : 0,
        "medium" : 1,
        "low" : 2
    }
    if not projects:
        return []
    return sorted(projects,key=lambda project : (priority[project["priority"]],-project["overdue_days"]))
   

project_report = generate_project_report(projects)
print(project_report)