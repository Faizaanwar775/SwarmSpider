import json


def write_failed(record, reason):

    with open(
        "reports/failed_pages.jsonl",
        "a",
        encoding="utf-8",
    ) as f:

        f.write(
            json.dumps(
                {
                    "reason": reason,
                    "record": record,
                },
                default=str,
            )
            + "\n"
        )