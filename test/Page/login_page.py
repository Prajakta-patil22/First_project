import time
from test.Locator.login_locator import LoginLocator
from test.Utilities.BrowserUtilities import BrowserUtility

class LoginPage:

    @staticmethod
    def env_url(browser):
        time.sleep(2)  # Ideally, use WebDriverWait

    @staticmethod
    def click_login_link(browser):
        element = LoginLocator.login_link
        BrowserUtility.click(browser, element)

    @staticmethod
    def click_login_option(browser):
        element = LoginLocator.login_option
        BrowserUtility.click(browser, element)

    @staticmethod
    def enter_email(browser):
        element = LoginLocator.email_id
        text = "prajakta1998patil@gmail.com"
        BrowserUtility.enter_text(browser, element, text)

    @staticmethod
    def enter_password(browser):
        element = LoginLocator.password
        text = "Stat2020$"
        BrowserUtility.enter_text(browser, element, text)

    @staticmethod
    def click_signin_btn(browser):
        element = LoginLocator.signin_btn
        BrowserUtility.click(browser, element)
        time.sleep(2)
