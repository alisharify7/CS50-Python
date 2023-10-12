import re
import sys
from datetime import date
from inflect import engine


class HumanLiveTime:

    def __init__(self, date):
        self.date = date

    def calculate(self, date: date):
        self.total_minute = self.get_total_minute(date)
        return self.get_total_minute_p(self.total_minute)

    def get_total_minute(self, date: date):
        return round((date.today() - date).total_seconds() / 60)

    def get_total_minute_p(self, date):
        e = engine()
        return (e.number_to_words(date, andword="").capitalize() + " minutes")


def main():
    human = HumanLiveTime()
    birth_date = input("Date of Birth: ").strip()

    if not (birth_date := is_valid_birth_date(birth_date)):
        sys.exit("Invalid date")

    print(human.calculate(birth_date))


def is_valid_birth_date(birth_date: str) -> bool:
    """
    Validates a birth date.

    Args:
        birth_date: The birth date in the format YYYY-MM-DD.

    Returns:
        True if the birth date is valid, False otherwise.

    Raises:
        ValueError if the birth date is not in the correct format.
    """

    try:
        d = date.fromisoformat(birth_date)
        return [d.year, d.month, d.day]
    except ValueError:
        return False

    #                with regex
    # regex = r"^\d{4}-\d{2}-\d{2}$"

    #                with out regex
    # dates = x.split("-")
    # if len(dates) != 3:
    #     sys.exit("Invalid date")

    # for each in dates:
    #     if not each.isdigit():
    #         sys.exit("Invalid date")

    # try:
    #     return date(*[int(each) for each in dates])
    # except Exception as e:
    #     sys.exit("Invalid date")


if __name__ == "__main__":
    main()
