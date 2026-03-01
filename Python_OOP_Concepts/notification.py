class Notification:
    def send_message(self):
        print("Sending notification...")
class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email.")
        print("Connecting to email server...")
class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS.")
        print("Sending through mobile network...")
class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via App.")
        print("Pushing notification to mobile app...")
def notify_user(notification_type):
    notification_type.send_message()
email = EmailNotification()
sms = SMSNotification()
app = AppNotification()
print("Email Notification:")
notify_user(email)
print("\nSMS Notification:")
notify_user(sms)
print("\nApp Notification:")
notify_user(app)