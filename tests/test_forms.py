import pytest
from pages.forms import FormsPage

@pytest.fixture
def forms_page(home_page, browser):
    home_page.clickFormsCard()
    return FormsPage(browser)

def test_practice_form_nav(forms_page):
    forms_page.clickPracticeFormItem()
    load = forms_page.verifyPracticeFormNavSuccessful()
    assert load is True
