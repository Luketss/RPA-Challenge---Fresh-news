import re
import csv
import datetime
import requests
import uuid


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


def replace_date_with_hour(date: str) -> str:
    if re.match("\d\w ago", date):
        return f"{datetime.datetime.now().strftime('%b')} {datetime.datetime.now().day}"
    return date


def write_csv_data(data: list) -> None:
    with open("resultado.csv", "w") as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        writer.writerows(data)


def download_image_from_url(image_url: str):
    # this need to be checked, i don't think all the images are present in a six month range
    image_name = str(uuid.uuid4())
    if image_url == "":
        return ""
    img_data = requests.get(image_url).content
    with open(f"./images/{image_name}.jpg", "wb", encoding="utf-8") as handler:
        handler.write(img_data)
    return image_name


def check_for_dolar_sign(text: str) -> bool:
    pattern = r"\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*(?:dollars|USD)?"

    if re.search(pattern, text):
        return True
    return False


def split_extracted_text(text: list) -> tuple[str, str]:
    try:
        date, title, description, *r_date = text

        return date, title, description
    except:
        return "", "", ""


if __name__ == "__main__":
    print(set_month_range(1))
