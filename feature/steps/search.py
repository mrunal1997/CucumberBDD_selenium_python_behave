from behave import given, when, then
from selenium.webdriver import Chrome
from time import sleep


@given('I am on the login page')
def open_browser(context):
    context.driver = Chrome()
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    context.driver.maximize_window()


@when('I enter username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    username_input = context.driver.find_element("xpath", "//input[@id='username']")
    username_input.send_keys(username)
    password_input = context.driver.find_element("xpath", "//input[@id='password']")
    password_input.send_keys(password)


@when('I click the login button')
def login_btn(context):
    login_button = context.driver.find_element("xpath", "//button[@id='submit']")
    login_button.click()


@then('I should be logged in successfully')
def message(context):
    assert "Logged In Successfully" in context.driver.title
    sleep(3)
    context.driver.quit()


@then('I should see an error message')
def message_error(context):
    error_message = context.driver.find_element("xpath", "//div[@id='error']")
    sleep(3)
    assert error_message.is_displayed()
    context.driver.quit()
