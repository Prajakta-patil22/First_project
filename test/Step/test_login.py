from pytest_bdd import scenarios, then, given, when, parsers

from test.Page.login_page import Login_page

scenarios('../Feature/login.feature')


@when('User visit test environment')
def visit_url(browser):
    Login_page.env_url(browser)
