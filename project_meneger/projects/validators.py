from django.core.exceptions import ValidationError
import datetime

def validate_deadline(value):
    today=datetime.date.today()
    if value <= today:
        raise ValidationError('Deadline must be in the future.')