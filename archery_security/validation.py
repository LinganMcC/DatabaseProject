
VALID_ROUNDS = [
    "WA90/1440",
    "WA70/1440",
    "WA60/1440",
    "AA50/1440",
    "AA40/1440"
]

def validate_archer_id(value):
    if not str(value).isdigit():
        raise ValueError("ArcherID must be numeric")
    return int(value)

def validate_round_name(round_name):
    if round_name not in VALID_ROUNDS:
        raise ValueError("Invalid round name")
    return round_name

def validate_date(date_text):
    parts = date_text.split("-")

    if len(parts) != 3:
        raise ValueError("Date must be YYYY-MM-DD")

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Date contains invalid characters")

    return date_text

