"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence, one-star review of planet Earth by an alien
tourist that still slips in a genuine compliment about the food,
to /output/entry.txt.
"""

import os

ENTRY = (
    "One star: Earth glued my tentacles to the floor with gravity, "
    "its weather changed moods hourly, yet the dumplings were so good "
    "my third eye wept and I have applied for permanent residency."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
