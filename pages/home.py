from selenium.webdriver.common.by import By


class HomePage:
    # URL

    URL = "https://demoqa.com/"

    # Locators

    FORMS_CARD = (By.XPATH, "//h5[text()='Forms']")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def closeBanner(self):
        self.browser.execute_script("document.getElementById('fixedban').remove()");

    def clickFormsCard(self):
        forms_card = self.browser.find_element(*self.FORMS_CARD)
        self.browser.execute_script("arguments[0].scrollIntoView();", forms_card)
        forms_card.click()
