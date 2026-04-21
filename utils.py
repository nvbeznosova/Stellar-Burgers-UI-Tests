import random
import string

def generate_email():
    """Generate a unique email address for registration tests"""
    random_digits = random.randint(100, 999)  # 3 random digits
    return f"nadia_beznosova_31_{random_digits}@yandex.ru"

def generate_password(length=8):
    """Generate a random password for registration tests"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))
