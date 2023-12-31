import argparse
from csv import DictReader
import json
from pathlib import Path


def _sanitize_comment(comment: str) -> str:
    comment = comment.strip()
    return comment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path, help="Path to the CSV file to process.")
    parser.add_argument(
        "manual_file", type=Path, help="Path to the manual JSON additions/overrides."
    )
    parser.add_argument("output_file", type=Path, help="Output JSON file to write to.")

    parsed_args = parser.parse_args()

    with parsed_args.manual_file.open(encoding="utf-8") as fh:
        manual_data = json.load(fh)

    data = []
    reader = DictReader(parsed_args.csv_file.open(encoding="utf-8", newline=""))

    removes = set(manual_data["remove"])
    index = {}
    for row in sorted(reader, key=lambda item: item["Restaurant Name"]):
        if not row["Restaurant Name"].strip():
            continue

        if row["Restaurant Name"] in removes:
            continue

        comments = []
        if row["Notes"]:
            comments.append(_sanitize_comment(row["Notes"]))
        if row["Employee Comments"]:
            comments.append(_sanitize_comment(row["Employee Comments"]))

        autograt = False
        for comment in comments:
            lower_comment = comment.lower()
            if (
                "autograt" in lower_comment
                or "no-tipping" in lower_comment
                or "no tipping" in lower_comment
            ) and not ("or more" in lower_comment or "large group" in lower_comment):
                autograt = True
                break

        autograt |= True if row["Counts as tip?"] == "Y" else False

        fee_obj = {"percentage": row["Fee %"].replace("%", "")}
        if autograt:
            fee_obj["name"] = "Gratuity"

        data.append(
            {
                "name": row["Restaurant Name"],
                "fees": [fee_obj],
                "removable": row["Removable?"] == "Y",
                "comments": comments,
                "location": row["Location"],
                "autograt": autograt,
                "sources": [
                    "[Reddit /r/LosAngeles Restaurant Surcharges List](https://docs.google.com/spreadsheets/d/1EEPzeytrva770H2xPFFPDUUNdpnL_VQL4vbzFph-jus/edit?usp=drive_link)"
                ],
            }
        )
        index[row["Restaurant Name"]] = data[-1]

    for item in manual_data["add"]:
        if item["name"] in index:
            index[item["name"]].update(item)
        else:
            data.append(item)

    with parsed_args.output_file.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


if __name__ == "__main__":
    main()
