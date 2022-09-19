from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email_task(email_address, status=0, time=None):
    message = ""
    if status == 0:
        message = f"There is a request for your taxi.\n\nTaxi A.Ş"
    elif status == 1 and time:
        message = f"Your taxi request has been approved. It will be with you in {time}.\n\nTaxi A.Ş"
    elif status == 2:
        message = f"Your taxi request was declined.\n\nTaxi A.Ş"

    if message:
        send_mail(
            "Notification!",
            message,
            "appinventourist@gmail.com",
            [email_address],
        )
