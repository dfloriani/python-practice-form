from selenium.webdriver.common.by import By


class FormsPage:
    # URL

    URL = "https://demoqa.com/forms"

    # Locators

    PRACTICE_FORM_ITEM = (By.XPATH, "//span[text()='Practice Form']")
    PRACTICE_FORM = (By.ID, "userForm")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def clickPracticeFormItem(self):
        practice_form_item = self.browser.find_element(*self.PRACTICE_FORM_ITEM)
        practice_form_item.click()

    def verifyPracticeFormNavSuccessful(self):
        element = self.browser.find_element(*self.PRACTICE_FORM)
        return element.is_displayed()

