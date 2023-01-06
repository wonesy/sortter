import pytest

from sortter.support_request import SUPER_NAIVE_EMAIL_REGEX, SUPER_NAIVE_PHONE_REGEX

@pytest.mark.parametrize("email", [
    ("s@s.s"),
    ("something@123.333s"),
])
def test_valid_email_regex(email: str):
    assert SUPER_NAIVE_EMAIL_REGEX.match(email) is not None

@pytest.mark.parametrize("email", [
    ("s@s."),
    ("@123.333s"),
    ("123.333s"),
    ("asdf@123."),
])
def test_invalid_email_regex(email: str):
    assert SUPER_NAIVE_EMAIL_REGEX.match(email) is None

@pytest.mark.parametrize("phone", [
    ("0000000000"),
    ("1234567890"),
    ("0406104444"),
    ("0358406104444"),
    ("+358406104444"),
    ("+000000000000"),
])
def test_valid_phone_regex(phone: str):
    assert SUPER_NAIVE_PHONE_REGEX.match(phone) is not None

@pytest.mark.parametrize("phone", [
    ("000000000"),
    ("12345678900"),
    ("+0406104444"),
    ("358406104444"),
    ("00000000000"),
])
def test_invalid_phone_regex(phone: str):
    assert SUPER_NAIVE_PHONE_REGEX.match(phone) is None