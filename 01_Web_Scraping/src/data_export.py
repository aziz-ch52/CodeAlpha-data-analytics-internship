from pathlib import Path
from typing import Dict, List
import json
import pandas as pd


def export_data(
    raw_records: List[Dict],
    cleaned_df: pd.DataFrame,
    base_dir: Path | None = None,
) -> None:
    """Save raw JSON/CSV and processed CSV/JSON outputs."""
    project_root = base_dir or Path(__file__).resolve().parents[1]
    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"

    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    # Save raw data
    raw_json_path = raw_dir / "books_raw.json"
    with open(raw_json_path, "w", encoding="utf-8") as f:
        json.dump(raw_records, f, indent=2, ensure_ascii=False)

    pd.DataFrame(raw_records).to_csv(raw_dir / "books_raw.csv", index=False, encoding="utf-8")

    # Save processed data
    cleaned_df.to_csv(processed_dir / "books_cleaned.csv", index=False, encoding="utf-8")
    cleaned_df.to_json(processed_dir / "books_cleaned.json", orient="records", indent=2)