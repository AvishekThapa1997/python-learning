from collections import defaultdict
from typing import Literal, TypedDict


class Order(TypedDict):
    status: Literal["pending","completed","failed"]




orders : list[Order] = [
    {"status": "completed"},
    {"status": "pending"},
    {"status": "completed"},
    {"status": "failed"},
    {"status": "pending"},
]




def generate_status_report(reports : list[Order]):
    result: defaultdict  = defaultdict(int)
    for report in reports:
        result[report.get("status")] += 1
    return dict(result)



print(generate_status_report(reports=orders))