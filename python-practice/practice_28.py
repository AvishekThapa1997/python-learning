from abc import ABC, abstractmethod
from typing import Generic, Literal, TypedDict, TypeVar

T = TypeVar("T")

class JobProcessor(ABC, Generic[T]):

    @abstractmethod
    def process(self, payload:T) -> None:
        pass


class EmailPayload(TypedDict):
    to:str
    subject: str

class ReportPayload(TypedDict):
    report_id:str
    format : Literal["pdf" , "txt"]

class EmailJobProcessor(JobProcessor[EmailPayload]):
    def process(self, payload):
        print("Processing Email Job",payload)


class ReportJobProcessor(JobProcessor[ReportPayload]):
    def process(self, payload):
        print("Processing Report Job", payload)

email_job_processor : JobProcessor[EmailPayload] = EmailJobProcessor()
email_job_processor.process({
    "subject":"test",
    "to":"tets"
})
report_processor = ReportJobProcessor()
report_processor.process({
    "report_id": "RPT-101",
    "format": "pdf",
})