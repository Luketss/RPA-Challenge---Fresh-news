import datetime


def set_month_range(number_of_months: int) -> tuple[str, str]:
    today = datetime.date.today()
    end = today.strftime("%m/%d/%Y")
    if number_of_months < 2:
        start = today.replace(day=1).strftime("%m/%d/%Y")
    else:
        start = (
            (today - datetime.timedelta(days=30 * (number_of_months - 1)))
            .replace(day=1)
            .strftime("%m/%d/%Y")
        )
    return start, end


if __name__ == "__main__":
    print(set_month_range(1))
