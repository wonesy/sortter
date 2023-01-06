import re

from pydantic import BaseModel, validator

# not going to truly validate this - just make sure it's something like x@x.x
SUPER_NAIVE_EMAIL_REGEX = re.compile(r'.+@.+[.].+')

# this is complicated, so i'll just make sure this is either
# - 10 digits e.g. 0401234567
# - 12 digits with a leading (+) or (0) e.g. +358401234567 / 0358401234567
SUPER_NAIVE_PHONE_REGEX = re.compile(r'(^\d{10}$)|(^\+\d{12}$)|(^0\d{12}$)')


class SupportRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    description: str

    @validator("email")
    def validate_email(cls, v):
        assert SUPER_NAIVE_EMAIL_REGEX.match(v)
        return v

    @validator("phone")
    def validate_phone(cls, v):
        assert SUPER_NAIVE_PHONE_REGEX.match(v)
        return v