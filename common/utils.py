"""
Utility functions for Django projects.
"""

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(subject, recipient_list, template, context):
    """
    Utility function to send HTML email using Django's send_mail function.
    :param subject: Subject of the email
    :param recipient_list: List of recipients
    :param template: Template name (HTML file)
    :param context: Context data for rendering the template
    :return: None
    """
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, 'your_email@example.com', recipient_list, html_message=html_message)


def calculate_age(birth_date):
    """
    Utility function to calculate age based on birth date.
    :param birth_date: Date of birth
    :return: Age
    """
    import datetime
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


