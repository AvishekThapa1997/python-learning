from abc import ABC, abstractmethod

# class Notifier(ABC):
#     @abstractmethod
#     def notify(self, message: str) -> None:
#         pass
# class EmailNotifier(Notifier):
#     def notify(self, message: str) -> None:
#         print(f"Email Notification {message}")
# class SMSNotifier(Notifier):
#     def notify(self, message) -> None:
#         print(f"SMS Notification {message}")
# Using Protocol
from typing import Protocol


class Notifier(Protocol):
    def notify(self, message: str) -> None:
        pass


class EmailNotifier:
    def notify(self, message: str) -> None:
        print(f"Email Notification {message}")


class SMSNotifier:
    def notify(self, message: str) -> None:
        print(f"SMS Notification {message}")


def send_notification(notifier: Notifier, message: str):
    notifier.notify(message)


email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

send_notification(email_notifier, "Hello I am from email")
send_notification(sms_notifier, "Hello I am from sms")


class MessageNotifier(Protocol):
    def post_message(self, channel: str, message: str) -> None:
        pass


class SlackClient:
    def post_message(self, channel: str, message: str) -> None:
        print(f"Posting to {channel}: {message}")


def send_alert(client: MessageNotifier, channel: str, message: str) -> None:
    client.post_message(channel, message)


slack_client = SlackClient()

send_alert(
    slack_client,
    channel="dev-channel",
    message="Hello team!",
)
