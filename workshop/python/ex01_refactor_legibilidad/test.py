from before import format_user_message as b
from after import format_user_message as a


def run():
    cases = [
        (None, "admin", None, False),
        (" ", "admin", 31, False),
        ("Ana", "admin", 5, False),
        ("Ana", "user", 61, False),
        ("Ana", "user", None, False),
        ("Ana", "guest", 1, False),
        ("Ana", "user", 1, True),
    ]

    for c in cases:
        assert b(*c) == a(*c), (c, b(*c), a(*c))

    print("OK: comportamiento idéntico")


if __name__ == "__main__":
    run()