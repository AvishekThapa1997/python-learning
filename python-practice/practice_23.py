class BaseEvent:
    def __init__(self, **kwargs):
        print("BaseEvent initialized")
        super().__init__(**kwargs)


class ValidateEvent(BaseEvent):
    def __init__(self, **kwargs):
        print("ValidateEvent initialized")
        super().__init__()
        # TODO


class AuditEvent(BaseEvent):
    def __init__(self, **kwargs):
        print("AuditEvent initialized")
        super().__init__()


class EventProcessor(ValidateEvent, AuditEvent):
    def __init__(self, event_id: str):
        super().__init__()
        self.event_id = event_id      