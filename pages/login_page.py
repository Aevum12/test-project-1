from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert ('login' in current_url), 'No "Login" in url'

    def should_be_login_form(self):
        email = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        assert email and password, 'There is no Email input or Password input'

    def should_be_register_form(self):
        email = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
        password = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD)
        repeat_password = self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        assert email and password and repeat_password, 'There is no registration email, password or repeat password input'
