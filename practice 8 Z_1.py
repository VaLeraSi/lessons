import re


def email_parse(email_adr):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_adr):
        raise ValueError(f"wrong email: {email_adr}")
    print(RE_email.match(email_adr).groupdict())


try:
    email_parse("someone@geekbrains.ru")
    email_parse("someonegeekbrains.ru")
    email_parse("someonegeekbrainsru")
except ValueError as err:
    print(err)
