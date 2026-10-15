# Vaccination Tracker

A small, modular Python program for tracking vaccination records by anonymous ID. Built as a university OOP assignment using only the Python standard library (Python 3.8+).

This project follows Digital Public Goods (DPG) principles: it is open-source (MIT), inclusive (age-group categories rather than personal identity), privacy-respecting (no names, phone numbers, addresses, or other personal data), and split into reusable modules.

## Features

- Vaccine schedules — define a vaccine with a name, number of doses (at least 1), and days between doses (0 or greater)
- Anonymous registration — create records with generated IDs (`VR-0001`, `VR-0002`, …) and an age group (`infant`, `child`, `adolescent`, `adult`)
- Dose tracking — record a dose (defaults to today’s date), refuse extra doses once the schedule is complete, and compute the next due date
- Status — mark each record as `COMPLETE` or `IN PROGRESS` from doses received vs required
- Age-group updates — change a record’s age group with the same validation as registration
- Dictionary store — add records by ID (duplicate IDs are rejected), list all records, and summarise totals (all, fully vaccinated, in progress)
- OOP patterns — instance methods, `@classmethod` (`register`, `total_registered`), `@staticmethod` (`is_valid_age_group`), and a class constant for age groups
- Standard library only — Python 3.8+, no third-party packages

## Privacy

Records use generated IDs such as `VR-0001`. Age group is the only demographic field (`infant`, `child`, `adolescent`, `adult`). Do not add names or other identifiable information.

## Requirements

- Python 3.8 or later
- No third-party packages

On this Mac, use `python3` (not `python`):

```bash
python3 --version

## How to run

From the project root:

```bash
python3 main.py
```

The demo creates two vaccines (Measles and Polio (OPV)), registers three anonymous records, records some doses, prints each record, and prints a summary.

## Project structure

| File | Role |
| --- | --- |
| `models.py` | `Vaccine` and `VaccinationRecord` classes |
| `tracker.py` | Dictionary-based add, display, and summary functions |
| `main.py` | Demo program |
| `LICENSE` | MIT License |
| `README.md` | This file |

Storage is a dictionary keyed by `record_id`. Lists are not used as the record store.

## License

MIT. See `LICENSE`.
