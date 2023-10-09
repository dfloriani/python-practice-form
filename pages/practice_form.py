from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


class PracticeFormPage:
    # URL

    URL = "https://demoqa.com/automation-practice-form"

    # Locators

    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    MOBILE_INPUT = (By.ID, "userNumber")
    FORM_ID = (By.ID, "userForm")
    STATE_INPUT = (By.XPATH, "//*[@id='state']//input")
    STATE_SELECTED = (By.XPATH, "//div[@id='state']//div[contains(@class, 'singleValue')]")
    CITY_INPUT = (By.XPATH, "//div[@id='city']//input")
    CITY_SELECTED = (By.XPATH, "//div[@id='city']//div[contains(@class, 'singleValue')]")
    DOB_INPUT = (By.ID, "dateOfBirthInput")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DAY_OPTION = (By.XPATH, "//div[@class='react-datepicker__week']/div")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    SUBJECT_ITEMS = (By.XPATH, "//div[contains(@class, 'multiValue')]")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type=checkbox]")

    # Modal
    MODAL_HEADER = (By.XPATH, "//*[@class='modal-header']//div[text()='Thanks for submitting the form']")
    MODAL_TABLE_STUDENT_NAME_ROW = (By.XPATH, "//td[text()='Student Name']//following-sibling::td")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def closeBanners(self):
        self.browser.execute_script("document.getElementById('Ad.Plus-728x90').remove()");
        self.browser.execute_script("document.getElementById('fixedban').remove()");

    def enterFirstName(self, name):
        first_name_input = self.browser.find_element(*self.FIRST_NAME_INPUT)
        first_name_input.send_keys(name)

    def enterLastName(self, lastName):
        last_name_input = self.browser.find_element(*self.LAST_NAME_INPUT)
        last_name_input.send_keys(lastName)

    def selectGender(self, gender):
        gender_radio = self.browser.find_element(By.XPATH, "//input[@value='" + gender + "']/..")
        gender_radio.click()

    def enterMobile(self, mobile):
        mobile_input = self.browser.find_element(*self.MOBILE_INPUT)
        mobile_input.send_keys(mobile)

    def selectState(self, state):
        state_input = self.browser.find_element(*self.STATE_INPUT)
        state_input.send_keys(state + Keys.ENTER)

    def verifyStateSelected(self, state):
        state_selected = self.browser.find_element(*self.STATE_SELECTED)
        return state_selected.text == state

    def verifyCityDefaultDisabled(self):
        city_input = self.browser.find_element(*self.CITY_INPUT)
        return city_input.is_enabled()

    def selectCity(self, city):
        city_input = self.browser.find_element(*self.CITY_INPUT)
        city_input.send_keys(city + Keys.ENTER)

    def verifyCitySelected(self, city):
        city_selected = self.browser.find_element(*self.CITY_SELECTED)
        return city_selected.text == city

    def selectSubjects(self, subjects):
        subject_input = self.browser.find_element(*self.SUBJECTS_INPUT)
        for subject in subjects:
            subject_input.send_keys(subject)
            subject_input.send_keys(Keys.ENTER)
            WebDriverWait(self.browser, 20)\
                .until(expected_conditions
                       .visibility_of_element_located((By.XPATH,
                                                       "//div[contains(@class, 'multiValue')]//div[text()='"
                                                       + subject + "']")))

    def verifySubjectsSelected(self, subjects):
        subject_items = self.browser.find_elements(*self.SUBJECT_ITEMS)
        return len(subject_items) == len(subjects)

    def selectDate(self, month, year):
        dob_input = self.browser.find_element(*self.DOB_INPUT)
        dob_input.click()

        WebDriverWait(self.browser, 20)\
            .until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".react-datepicker-popper")))

        dob_month = self.browser.find_element(*self.MONTH_DROPDOWN)
        sel = Select(dob_month)
        sel.select_by_visible_text(month)

        dob_year = self.browser.find_element(*self.YEAR_DROPDOWN)
        sel = Select(dob_year)
        sel.select_by_value(year)

        day_week = self.browser.find_element(*self.DAY_OPTION)
        day_week.click()

    def verifyDate(self, dateText):
        dob_input = self.browser.find_element(*self.DOB_INPUT)
        return dob_input.get_attribute("value") == dateText

    def selectHobbies(self):
        hobbies_checkboxes = self.browser.find_elements(*self.CHECKBOXES)
        for checkbox in hobbies_checkboxes:
            # Using JS to avoid the 'click intercepted' error
            self.browser.execute_script("arguments[0].click();", checkbox)

    def verifyHobbiesSelected(self):
        checked = 0;
        hobbies_checkboxes = self.browser.find_elements(*self.CHECKBOXES)
        for checkbox in hobbies_checkboxes:
            if checkbox.is_selected():
                checked += 1
        return checked

    def submitForm(self):
        form = self.browser.find_element(*self.FORM_ID)
        form.submit()

    def verifySubmitSuccessful(self, firstName, lastName):
        modal_header = self.browser.find_element(*self.MODAL_HEADER)
        student_name_row = self.browser.find_element(*self.MODAL_TABLE_STUDENT_NAME_ROW)
        return modal_header.is_displayed() and student_name_row.text == firstName + ' ' + lastName
        # could check other rows as well with an 'and'

    def verifySubmitFailed(self):
        # required fields should receive a red border
        first_name = self.browser.find_element(*self.FIRST_NAME_INPUT)
        return first_name.value_of_css_property("border-color") == "rgb(220, 53, 69)"
        # could check other fields as well with an 'and'

