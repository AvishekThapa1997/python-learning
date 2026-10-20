
class Notification:
    message: str

    def __init__(self, message : str):
        self.message  = message

    @classmethod
    def from_dict(cls, notification_data):
        return cls(**notification_data)

    def send(self):
        return "PARENT NOTIFICATION"

class EmailNotification(Notification):
    message : str
    recipient: str

    def __init__(self, recipient: str, **kwargs):
       super().__init__(**kwargs)
       self.recipient = recipient

    def send(self):
        super().send()
        return "SEND EMAIL NOTIFICATION"   


class SMSNotification(Notification):

    phone_number: str
    def __init__(self, phone_number:str,**kwargs):
        super().__init__(**kwargs)
        self.phone_number = phone_number

    def send(self):
        super().send()
        return "SMS NOTIFICATION"    
        
       

email = EmailNotification.from_dict({
    "message": "Build completed",
    "recipient": "dev@example.com",
})

sms = SMSNotification.from_dict({
    "message": "Build failed",
    "phone_number": "+911234567890",
})

class NotificationHelper(SMSNotification, EmailNotification):
    pass

print(type(email).__name__)  # EmailNotification
print(type(sms).__name__)    # SMSNotification
print(email.recipient)       # dev@example.com
print(sms.phone_number)      # +911234567890


print(NotificationHelper(phone_number="ddd", message="ddd",recipient="dev@example.com").send())