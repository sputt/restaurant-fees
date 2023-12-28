import argparse
from csv import DictReader
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path, help="Path to the CSV file to process.")
    parser.add_argument("output_file", type=Path, help="Output JSON file to write to.")

    parsed_args = parser.parse_args()

    data = []
    reader = DictReader(parsed_args.csv_file.open(encoding="utf-8", newline=""))
    for row in reader:
        if not row["Restaurant Name"].strip():
            continue
        data.append(
            {
                "name": row["Restaurant Name"],
                "fees": [{"percentage": row["Fee %"].replace("%", "")}],
                "removable": row["Removable?"] == "Y",
                "comments": row["Notes"],
            }
        )

    with parsed_args.output_file.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


if __name__ == "__main__":
    main()
