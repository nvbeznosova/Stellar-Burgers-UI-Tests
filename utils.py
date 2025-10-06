import random
import string

def generate_email():
    """Генерирует уникальный email для теста регистрации"""
    random_digits = random.randint(100, 999)  # любые 3 цифры
    return f"nadia_beznosova_31_{random_digits}@yandex.ru"

def generate_password(length=8):
    """Генерирует случайный пароль"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))
