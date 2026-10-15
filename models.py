from datetime import date, timedelta


class Vaccine:
    "A reusable vaccine definition (type, schedule). No personal data."

    def __init__(self, name, doses_required, interval_days):
        if doses_required < 1:
            raise ValueError("doses_required must be at least 1")
        if interval_days < 0:
            raise ValueError("interval_days must be 0 or greater")
        self.name = name
        self.doses_required = doses_required
        self.interval_days = interval_days

    def display_info(self):
        return (
            f"{self.name}: {self.doses_required} dose(s), "
            f"{self.interval_days} day(s) between doses"
        )


class VaccinationRecord:
    # ""Anonymous vaccination record identified only by a generated ID.""

    AGE_GROUPS = ("infant", "child", "adolescent", "adult")
    _counter = 0

    def __init__(self, record_id, age_group, vaccine):
        if not VaccinationRecord.is_valid_age_group(age_group):
            raise ValueError(
                f"Invalid age_group {age_group!r}. "
                f"Must be one of {VaccinationRecord.AGE_GROUPS}"
            )
        if not isinstance(vaccine, Vaccine):
            raise ValueError("vaccine must be a Vaccine object")
        self.record_id = record_id
        self.age_group = age_group
        self.vaccine = vaccine
        self.doses_received = 0
        self.last_dose_date = None

    @classmethod
    def register(cls, age_group, vaccine):
        if not cls.is_valid_age_group(age_group):
            raise ValueError(
                f"Invalid age_group {age_group!r}. "
                f"Must be one of {cls.AGE_GROUPS}"
            )
        cls._counter += 1
        record_id = f"VR-{cls._counter:04d}"
        return cls(record_id, age_group, vaccine)

    @classmethod
    def total_registered(cls):
        return cls._counter

    @staticmethod
    def is_valid_age_group(age_group):
        return age_group in VaccinationRecord.AGE_GROUPS

    def record_dose(self, dose_date=None):
        if self.is_fully_vaccinated():
            return False
        self.doses_received += 1
        self.last_dose_date = date.today() if dose_date is None else dose_date
        return True

    def update_record(self, age_group):
        if not VaccinationRecord.is_valid_age_group(age_group):
            raise ValueError(
                f"Invalid age_group {age_group!r}. "
                f"Must be one of {VaccinationRecord.AGE_GROUPS}"
            )
        self.age_group = age_group

    def is_fully_vaccinated(self):
        return self.doses_received >= self.vaccine.doses_required

    def next_dose_due(self):
        if self.is_fully_vaccinated() or self.last_dose_date is None:
            return None
        return self.last_dose_date + timedelta(days=self.vaccine.interval_days)

    def display_info(self):
        status = "COMPLETE" if self.is_fully_vaccinated() else "IN PROGRESS"
        next_due = self.next_dose_due()
        next_text = next_due.isoformat() if next_due else "N/A"
        return (
            f"{self.record_id} | {self.age_group} | {self.vaccine.name} | "
            f"{self.doses_received}/{self.vaccine.doses_required} | "
            f"{status} | next dose: {next_text}"
        )
