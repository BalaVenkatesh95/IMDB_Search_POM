# pages/name_search_page.py
from base_page import BasePage
from ..utils.helpers import wait_for_element
from ..utils.helpers import element_clickable
from ..utils.screenshot import take_screenshot



class NameSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.awards_drop_down_button = "//div[text()='Awards & recognition']"
        self.award_nominated_button = "//button[@data-testid='test-chip-id-oscar_best_actor_nominees']"
        self.name_dropdown_button = "//div[@class='sc-6addea7c-0 dWrCpn' and text()='Name']"
        self.name_input_field = "//input[@name='name-text-input']"
        self.gender_dropdown_button = "//div[text()='Gender identity']"
        self.gender_male_button = "//button[@data-testid='test-chip-id-MALE']"
        self.see_results_button = "//span[text()='See results']"

    def name_search(self, name):
        if self.initiation_function():
            self.driver.execute_script("window.scrollBy(0, 750);")
            awards_drop_down_button = element_clickable(self.driver, self.awards_drop_down_button)
            self.click_element(awards_drop_down_button)

            award_nominated_button = element_clickable(self.driver, self.award_nominated_button)
            self.click_element(award_nominated_button)

            self.driver.execute_script("window.scrollBy(0, -400);")
            name_dropdown_button = wait_for_element(self.driver, self.name_dropdown_button)
            name_dropdown_button = element_clickable(self.driver, self.name_dropdown_button)
            self.click_element(name_dropdown_button)

            name_input_field = wait_for_element(self.driver, self.name_input_field)
            self.enter_text(name_input_field, name)

            self.driver.execute_script("window.scrollBy(0, 1100);")
            gender_dropdown_button = wait_for_element(self.driver, self.gender_dropdown_button)
            gender_dropdown_button = element_clickable(self.driver, self.gender_dropdown_button)
            self.click_element(gender_dropdown_button)

            gender_male_button = element_clickable(self.driver, self.gender_male_button)
            self.click_element(gender_male_button)

            see_results_button = wait_for_element(self.driver, self.see_results_button)
            self.click_element(see_results_button)
            take_screenshot(self.driver)

        else:
            return False

