import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value == "me":
        raise ValidationError(
            ('Использовать имя "me" в качестве username запрещено.'),
            params={"value": value},
        )
    if re.search(r"^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$", value) is None:
        raise ValidationError(
            (f"Не допустимые символы <{value}> в username."),
            params={"value": value},
        )
    return value
