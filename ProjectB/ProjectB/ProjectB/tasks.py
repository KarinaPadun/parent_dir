from celery import shared_task

@shared_task
def send_message(recipient, message):
    return f"Message '{message}' sent to {recipient}"
