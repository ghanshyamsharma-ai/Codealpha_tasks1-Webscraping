import csv
from pathlib import Path


DATA_FILE = Path("data/quotes.csv")

REQUIRED_COLUMNS = {"Quote", "Author", "Tags"}


def validate_dataset(file_path: Path) -> None:
    """Validate the scraped quotes dataset."""

    if not file_path.exists():
        print(f"Dataset not found: {file_path}")
        return

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print(" CSV file has no header.")
            return

        columns = set(reader.fieldnames)

        if not REQUIRED_COLUMNS.issubset(columns):
            print(
                f" Missing columns: "
                f"{REQUIRED_COLUMNS - columns}"
            )
            return

        rows = list(reader)

    if not rows:
        print(" Dataset is empty.")
        return

    empty_rows = 0

    for row in rows:
        if not row["Quote"].strip() or not row["Author"].strip():
            empty_rows += 1

    duplicate_count = len(rows) - len(
        {
            (
                row["Quote"].strip(),
                row["Author"].strip(),
            )
            for row in rows
        }
    )

    print(" Dataset validation successful!")
    print(f"Total records   : {len(rows)}")
    print(f"Columns         : {', '.join(reader.fieldnames)}")
    print(f"Empty records   : {empty_rows}")
    print(f"Duplicate rows  : {duplicate_count}")


if __name__ == "__main__":
    validate_dataset(DATA_FILE)