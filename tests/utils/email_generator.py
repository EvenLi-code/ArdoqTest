import random
import string


class EmailGenerator:
    @staticmethod
    def generate_email():
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        email = f"{prefix}@example.com"
        return email


if __name__ == "__main__":
    print(EmailGenerator.generate_email())
