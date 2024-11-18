import re


def valid_email(email):
# Перевіряє чи є email-адреса валідною.
# Регулярний вираз для перевірки email
    pattern = r'^[a-zA-Z0-9](\.?[a-zA-Z0-9])*@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(pattern, email))


emails = [
    "example@domain.com",
    "user.name@sub.domain.org",
    ".username@domain.com",
    "username.@domain.com",
    "user@domain.c",
    "user@domain.toolongtld",
    "user@domain1.com",
]

for email in emails:
    print(f"{email}: {'Валідний' if valid_email(email) else 'Невалідний'}")