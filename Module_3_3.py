import re

def normalize_phone(num):
    digits = re.sub(r"[^\d+]", "", num) # Delete all symbols except digits and +

    if digits.startswith("380"):
        return "+" + digits
    if digits[0].isdigit():
        return "+38" + digits
    if digits.startswith("+380"):
        return digits
    if re.match(r"^\+\d", digits):
        return digits

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+55  61377218sd76",
    "55  61377218sd76",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)
