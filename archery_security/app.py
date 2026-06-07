from validation import validate_archer_id
from queries import get_archer_history, get_personal_bests

print("=== Archery Database Security Demo ===")

try:
    archer_id = input("Enter Archer ID: ")

    # INPUT VALIDATION
    archer_id = validate_archer_id(archer_id)

    print("\n--- Score History ---")

    history = get_archer_history(archer_id)

    for row in history:
        print(row)

    print("\n--- Personal Bests ---")

    pbs = get_personal_bests(archer_id)

    for row in pbs:
        print(row)

except Exception as e:
    print("Error:", e)