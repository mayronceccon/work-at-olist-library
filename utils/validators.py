import datetime
from django.core.exceptions import ValidationError


def year_validator(year):
    if year < 0 or year > datetime.datetime.now().year + 1:
        raise ValidationError(
            "%(value)s is not a correct year!",
            params={"value": year},
        )
