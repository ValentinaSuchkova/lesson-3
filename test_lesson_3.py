from selene import browser, be, have

def test_positive_search(browser_setting):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative_search(browser_setting):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qwertyqwerty').press_enter()
    browser.element('[id="search"]').should(have.text('не найдено'))




