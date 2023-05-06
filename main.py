# docs for RPA lib > https://rpaframework.org/libdoc/RPA_Browser_Selenium.html
import time
from RPA.Browser.Selenium import Selenium

from setup import URL, SEARCH_PHRASE, NUMBER_OF_MONTHS
from util import set_month_range


class SeleniumScraper:
    def __init__(self):
        self.browser_lib = Selenium()

    def close_browser(self) -> None:
        self.browser_lib.close_browser()

    def open_website(self, url: str) -> None:
        self.browser_lib.open_available_browser(url)

    def begin_search(self, search_phrase: str):
        try:
            search_xpath = "//button[@class='css-tkwi90 e1iflr850']"  # try change
            self.browser_lib.click_button_when_visible(locator=search_xpath)
            field_xpath = "//input[@placeholder='SEARCH']"
            self.browser_lib.input_text(locator=field_xpath, text=search_phrase)
            go_button_xpath = "//button[@type='submit']"
            self.browser_lib.click_button_when_visible(locator=go_button_xpath)

        except ValueError as e:
            raise f"Error on execution of begin_search -> {e}"

    def select_category(self) -> None:
        try:
            section_drop_btn = "//div[@data-testid='section']//button[@type='button']"
            self.browser_lib.click_button_when_visible(locator=section_drop_btn)
            drop_path = "(//ul[@class='css-64f9ga'])[1]"

        except ValueError as e:
            raise f"Error on execution of select_category -> {e}"

    def sort_newest_news(self, list_value="newest") -> None:
        try:
            sort_dropdow_btn = "//select[@data-testid='SearchForm-sortBy']"
            self.browser_lib.select_from_list_by_value(sort_dropdow_btn, list_value)

        except ValueError as e:
            raise f"Error on execution of select_category -> {e}"

    def set_date_range(self, number_of_months: int) -> None:
        try:
            date_button = "//button[@data-testid='search-date-dropdown-a']"
            self.browser_lib.click_button_when_visible(locator=date_button)
            specific_dates_button = "//button[@value='Specific Dates']"
            self.browser_lib.click_button_when_visible(locator=specific_dates_button)
            input_date_range_start = "//input[@id='startDate']"
            input_date_range_end = "//input[@id='endDate']"
            date_start, date_end = set_month_range(number_of_months)
            self.browser_lib.input_text(input_date_range_start, date_start)
            self.browser_lib.input_text(input_date_range_end, date_end)
            self.browser_lib.click_button_when_visible(locator=date_button)

        except ValueError as e:
            raise f"Error on execution of select_category -> {e}"

    def extract_website_data(self):
        show_more_button = "//button[normalize-space()='Show More']"
        is_all_news_loaded = self.browser_lib.does_page_contain_button(show_more_button)
        while is_all_news_loaded:
            self.browser_lib.click_button_when_visible(show_more_button)

    def main(self) -> None:
        try:
            self.open_website(url=URL)
            self.begin_search(search_phrase=SEARCH_PHRASE)
            # self.select_category()
            self.sort_newest_news()
            self.set_date_range(NUMBER_OF_MONTHS)
            self.close_browser()
        except:
            self.close_browser()


if __name__ == "__main__":
    obj = SeleniumScraper()
    obj.main()
