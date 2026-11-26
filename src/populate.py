#!/usr/bin/env python3
import csv
import os
from pathlib import Path

import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
CSV_ENDPOINTS = {
    "users.csv": "users",
    "habits.csv": "habits",
    "challenge.csv": "challenges",
    "category.csv": "categories",
    "updates.csv": "updates",
}


def populate_csv(csv_path, endpoint, session):
    with csv_path.open(encoding="utf-8", newline="") as fd:
        rows = csv.DictReader(fd)
        if rows.fieldnames is None:
            raise ValueError(f"El archivo CSV no contiene encabezados: {csv_path}")

        for row_number, row in enumerate(rows, start=2):
            response = session.post(
                f"{BASE_URL}/{endpoint}",
                json=row,
                timeout=30,
            )
            response.raise_for_status()
            print(f"Insertado {csv_path.name}, fila {row_number}")


def main():
    data_dir = Path(__file__).resolve().parent
    csv_paths = {name: data_dir / name for name in CSV_ENDPOINTS}
    missing_files = [str(path) for path in csv_paths.values() if not path.is_file()]
    if missing_files:
        raise FileNotFoundError(
            "No se encontraron los siguientes archivos CSV:\n"
            + "\n".join(missing_files)
        )

    with requests.Session() as session:
        for filename, endpoint in CSV_ENDPOINTS.items():
            populate_csv(csv_paths[filename], endpoint, session)


if __name__ == "__main__":
    main()
