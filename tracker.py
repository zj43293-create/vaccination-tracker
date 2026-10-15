def add_record(records, record):
    """Add a record to the dictionary. Returns False if the ID already exists."""
    if record.record_id in records:
        return False
    records[record.record_id] = record
    return True


def display_records(records):
    """Print every record, or a message if the dictionary is empty."""
    if not records:
        print("No records found.")
        return
    for record in records.values():
        print(record.display_info())


def summary(records):
    """Return (total, fully_vaccinated, in_progress)."""
    total = len(records)
    fully_vaccinated = 0
    for record in records.values():
        if record.is_fully_vaccinated():
            fully_vaccinated += 1
    in_progress = total - fully_vaccinated
    return (total, fully_vaccinated, in_progress)
