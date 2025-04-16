# Treomind Datagen Project

This project was developed as part of the Treomind Data Bootcamp. It is a modular command-line interface (CLI) tool that reads structured datasets (CSV or Parquet), processes them in batches with optional shuffling and repetition, and writes the results to output CSV files.

---

## 🚀 Features

- ✅ Read CSV and Parquet files
- 🔀 Shuffle rows before batching
- 🔁 Repeat dataset multiple times
- 📦 Split data into configurable batch sizes
- 🕒 Add timestamp to each batch
- 💾 Save output batches to CSV
- 🧩 Modular architecture (`reader`, `processor`, `writer`, `utils`)
- 🛠️ Built using Python & Typer CLI

---

## 🗂️ Project Structure

```
treomind-datagen-project/
├── datagen/
│   ├── __main__.py       # CLI entry point
│   ├── reader.py         # Data reading logic
│   ├── processor.py      # Data batching logic
│   ├── writer.py         # Output writing logic
│   └── utils.py          # Versioning and paths
├── data/                 # Input data files (CSV / Parquet)
├── output/               # Generated output files
├── requirements.txt
└── README.md
```

---

## 🧪 Example Usage

```bash
python -m datagen generate \
  --input-file data/iris.csv \
  --extension csv \
  --batch-size 5 \
  --repeat 3 \
  --batch-interval 1.0 \
  --shuffle True \
  --prefix log_ \
  --output-folder output/ \
  --excluded-cols id \
  --output-index False
```

---

## ⚙️ CLI Options

| Option               | Description                                     |
|----------------------|-------------------------------------------------|
| `--input-file`       | Path to input file                              |
| `--extension`        | File type: `csv` or `parquet`                   |
| `--sep`              | Separator for CSV input                         |
| `--excluded-cols`    | Columns to exclude from input                   |
| `--batch-size`       | Rows per batch                                  |
| `--shuffle`          | Shuffle rows before batching                    |
| `--repeat`           | Repeat the full dataset N times                 |
| `--batch-interval`   | Seconds to wait between batches                 |
| `--output-folder`    | Folder to save output CSVs                      |
| `--prefix`           | Prefix for output filenames                     |
| `--output-index`     | Include index in output file                    |
| `--version`          | Show CLI version                                |

---

## 📦 Version

```bash
python -m datagen generate --version
```

---

## ✅ Git Flow Summary

This project was developed using Git best practices, including:
- Feature branches (`feature/extract`, `feature/transform`, `feature/load`)
- A `release/0.1.0` branch with versioning support
- A `develop` branch used for isolated utility logic (not merged)
- Final merge into `master` as per the Treomind bootcamp steps

---

## 🧑‍💻 Requirements

- Python 3.10+
- See `requirements.txt` for dependencies

To install:

```bash
pip install -r requirements.txt
```

---

## 📁 Sample Output

CSV batch files with `event_time` column saved to `/output` folder, e.g.:

```
output/
├── log_32f9bcab.csv
├── log_5fa8be61.csv
└── ...
```

---

## 🔗 Repo

[👉 View on GitHub](https://github.com/mertokten/treomind-datagen-project)

---

## 🙌 Credits

Project completed as part of the Treomind Data Bootcamp (Week 2 Homework).
