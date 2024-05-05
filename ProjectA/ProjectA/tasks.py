from celery import shared_task

@shared_task
def calculate_something(x, y):
    return x + y
