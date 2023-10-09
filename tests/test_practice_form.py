import pytest

from pages.practice_form import PracticeFormPage


@pytest.fixture
def practice_form_page(browser):
    pfp = PracticeFormPage(browser)
    pfp.load()
    pfp.closeBanners()
    return pfp

def test_submit_required(practice_form_page):
    firstName = "Dayane"
    lastName = "Floriani"
    mobile = "5555555555"
    gender = "Female"

    practice_form_page.enterFirstName(firstName)
    practice_form_page.enterLastName(lastName)
    practice_form_page.selectGender(gender)
    practice_form_page.enterMobile(mobile)
    practice_form_page.submitForm()
    submit = practice_form_page.verifySubmitSuccessful(firstName, lastName)
    assert submit is True

def test_submit_empty(practice_form_page):
    practice_form_page.submitForm()
    submit = practice_form_page.verifySubmitFailed()
    assert submit is True

def test_select_dob(practice_form_page):
    practice_form_page.selectDate("June", "2000")
    changed_date = practice_form_page.verifyDate("28 May 2000")
    assert changed_date is True

def test_select_hobbies(practice_form_page):
    practice_form_page.selectHobbies()
    result = practice_form_page.verifyHobbiesSelected()
    assert result == 3

def test_select_state(practice_form_page):
    state = "NCR"
    practice_form_page.selectState(state)
    result = practice_form_page.verifyStateSelected(state)
    assert result is True

def test_city_default_disabled(practice_form_page):
    enabled = practice_form_page.verifyCityDefaultDisabled()
    assert enabled is False

def test_select_city(practice_form_page):
    # Need to select state in order to enable city input
    state = "NCR"
    city = "Noida"
    practice_form_page.selectState(state)
    practice_form_page.selectCity(city)
    result = practice_form_page.verifyCitySelected(city)
    assert result is True

def test_select_subjects(practice_form_page):
    subjects = ['Maths', 'English', 'Computer Science']
    practice_form_page.selectSubjects(subjects)
    items_selected = practice_form_page.verifySubjectsSelected(subjects)
    assert items_selected is True
