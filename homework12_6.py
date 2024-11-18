import re

def strong_password(password):
    # Перевірка на мінімальну довжину
    if len(password) < 8:
        return False

    # вирази для паролів
    has_digit = re.search(r'\d', password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_special = re.search(r'[!@#$%^&*()_+{}":;\'<>?,./-]', password)
    return all([has_digit, has_upper, has_lower, has_special])

password = [
    'Qwerty123',
    'Qwerty@123',
    'qwerty123',
    'QWERTY123',
    'Qwer1',
    'Qwerty@2004!',
]

for pwd in password:
    print(f"Пароль '{pwd}': {'Надійний' if strong_password(pwd) else 'Ненадійний'}")