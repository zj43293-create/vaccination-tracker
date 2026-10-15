from models import Vaccine, VaccinationRecord
from tracker import add_record, display_records, summary


def main():
    records = {}

    measles = Vaccine("Measles", 2, 28)
    polio = Vaccine("Polio (OPV)", 3, 30)

    print("Vaccines")
    print(measles.display_info())
    print(polio.display_info())
    print()

    record_one = VaccinationRecord.register("infant", measles)
    record_two = VaccinationRecord.register("child", polio)
    record_three = VaccinationRecord.register("adult", measles)

    add_record(records, record_one)
    add_record(records, record_two)
    add_record(records, record_three)

    record_one.record_dose()
    record_two.record_dose()
    record_two.record_dose()
    record_three.record_dose()
    record_three.record_dose()

    print("Records")
    display_records(records)
    print()

    total, fully_vaccinated, in_progress = summary(records)
    print(
        f"Summary: total={total}, fully vaccinated={fully_vaccinated}, "
        f"in progress={in_progress}"
    )
    print(f"Total registered: {VaccinationRecord.total_registered()}")


if __name__ == "__main__":
    main()
