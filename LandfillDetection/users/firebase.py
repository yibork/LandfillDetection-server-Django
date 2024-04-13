import firebase_admin
from firebase_admin import messaging
from .models import User

def send_to_all(title, body):
    tokens = [user.fcm_token for user in User.objects.exclude(fcm_token__isnull=True)]
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        tokens=tokens,
    )
    response = firebase_admin.messaging.send_multicast(message)
    return response.success_count, response.failure_count
